// Command uni is the registrar of Anthropic University: it grades
// assignments and explorations by running their test suites, administers
// quizzes, records results as committed JSON, and reports progress toward
// the degree.
package main

import (
	"fmt"
	"math/rand/v2"
	"os"
	"strings"
	"time"
)

func main() {
	args := os.Args[1:]
	if len(args) == 0 {
		printUsage(os.Stderr)
		os.Exit(2)
	}
	command := args[0]
	if command == "hash" {
		os.Exit(runHash(args[1:]))
	}
	root, err := findRoot()
	if err != nil {
		fmt.Fprintln(os.Stderr, "error:", err)
		os.Exit(1)
	}
	curriculum, err := loadCurriculum(root)
	if err != nil {
		fmt.Fprintln(os.Stderr, "error:", err)
		os.Exit(1)
	}
	switch command {
	case "status":
		os.Exit(runStatus(root, curriculum, args[1:]))
	case "grade":
		os.Exit(runGrade(root, curriculum, args[1:]))
	case "quiz":
		os.Exit(runQuiz(root, curriculum, args[1:]))
	case "next":
		os.Exit(runNext(root, curriculum))
	case "help", "-h", "--help":
		printUsage(os.Stdout)
		os.Exit(0)
	default:
		fmt.Fprintf(os.Stderr, "unknown command: %s\n", command)
		printUsage(os.Stderr)
		os.Exit(2)
	}
}

func printUsage(out *os.File) {
	fmt.Fprint(out, `usage: uni <command>

  status               degree-level progress dashboard
  status <course>      detailed standing in one course (e.g. uni status 101)
  grade <course>/<item>  run an item's test suite and record the score
  quiz <course>/<item>   take a quiz interactively and record the score
  next                 what to work on next
  hash <salt> <answer> hash a quiz answer (for authoring quiz files)

  --dry on grade/quiz runs without recording a result
`)
}

func splitTarget(target string) (courseID, itemID string, err error) {
	parts := strings.SplitN(target, "/", 2)
	if len(parts) != 2 || parts[0] == "" || parts[1] == "" {
		return "", "", fmt.Errorf("expected <course>/<item>, e.g. 101/a1; got %q", target)
	}
	return parts[0], parts[1], nil
}

func resolveItem(root string, curriculum Curriculum, target string) (ref CourseRef, course Course, item Item, err error) {
	courseID, itemID, err := splitTarget(target)
	if err != nil {
		return CourseRef{}, Course{}, Item{}, err
	}
	ref, found := curriculum.findCourse(courseID)
	if !found {
		return CourseRef{}, Course{}, Item{}, fmt.Errorf("no course %q in curriculum.json", courseID)
	}
	course, authored, err := loadCourse(root, ref)
	if err != nil {
		return CourseRef{}, Course{}, Item{}, err
	}
	if !authored {
		return CourseRef{}, Course{}, Item{}, fmt.Errorf("course %s has no course.json yet", courseID)
	}
	item, found = course.findItem(itemID)
	if !found {
		return CourseRef{}, Course{}, Item{}, fmt.Errorf("no item %q in course %s", itemID, courseID)
	}
	return ref, course, item, nil
}

func popFlag(args []string, flag string) (remaining []string, present bool) {
	for _, arg := range args {
		if arg == flag {
			present = true
			continue
		}
		remaining = append(remaining, arg)
	}
	return remaining, present
}

func runStatus(root string, curriculum Curriculum, args []string) int {
	if len(args) > 0 {
		ref, found := curriculum.findCourse(args[0])
		if !found {
			fmt.Fprintf(os.Stderr, "no course %q in curriculum.json\n", args[0])
			return 1
		}
		course, authored, err := loadCourse(root, ref)
		if err != nil {
			fmt.Fprintln(os.Stderr, "error:", err)
			return 1
		}
		if !authored {
			fmt.Printf("%s — %s: content not yet authored\n", ref.ID, ref.Title)
			return 0
		}
		records, err := loadCourseRecords(root, ref.ID)
		if err != nil {
			fmt.Fprintln(os.Stderr, "error:", err)
			return 1
		}
		renderCourseStatus(os.Stdout, ref, course, records)
		return 0
	}
	standings, err := allStandings(root, curriculum)
	if err != nil {
		fmt.Fprintln(os.Stderr, "error:", err)
		return 1
	}
	renderDegreeStatus(os.Stdout, curriculum, standings)
	return 0
}

func allStandings(root string, curriculum Curriculum) (results []standing, err error) {
	for _, ref := range curriculum.Courses {
		course, authored, loadErr := loadCourse(root, ref)
		if loadErr != nil {
			return nil, loadErr
		}
		if !authored {
			results = append(results, standing{Ref: ref, Authored: false})
			continue
		}
		records, recordsErr := loadCourseRecords(root, ref.ID)
		if recordsErr != nil {
			return nil, recordsErr
		}
		results = append(results, computeStanding(ref, course, records))
	}
	return results, nil
}

func runGrade(root string, curriculum Curriculum, args []string) int {
	args, dry := popFlag(args, "--dry")
	if len(args) != 1 {
		fmt.Fprintln(os.Stderr, "usage: uni grade <course>/<item> [--dry]")
		return 2
	}
	ref, _, item, err := resolveItem(root, curriculum, args[0])
	if err != nil {
		fmt.Fprintln(os.Stderr, "error:", err)
		return 1
	}
	if item.Type == "quiz" {
		fmt.Fprintf(os.Stderr, "%s is a quiz; use: uni quiz %s\n", item.ID, args[0])
		return 2
	}
	result, err := runSuite(root, ref.Dir, item)
	if err != nil {
		fmt.Fprintln(os.Stderr, "error:", err)
		return 1
	}
	fmt.Print(result.Output)
	score := result.Score()
	fmt.Printf("\nScore: %.0f%% (%d/%d tests passing, pass bar %.0f%%)\n",
		score*100, result.Ran-result.Skipped-result.Failed-result.Errored,
		result.Ran-result.Skipped, curriculum.PassBar*100)
	if dry {
		fmt.Println("(dry run: not recorded)")
		return 0
	}
	record, err := recordAttempt(root, item, ref.ID, score, curriculum.PassBar, time.Now())
	if err != nil {
		fmt.Fprintln(os.Stderr, "error:", err)
		return 1
	}
	reportRecord(record)
	return 0
}

func runQuiz(root string, curriculum Curriculum, args []string) int {
	args, dry := popFlag(args, "--dry")
	if len(args) != 1 {
		fmt.Fprintln(os.Stderr, "usage: uni quiz <course>/<item> [--dry]")
		return 2
	}
	ref, _, item, err := resolveItem(root, curriculum, args[0])
	if err != nil {
		fmt.Fprintln(os.Stderr, "error:", err)
		return 1
	}
	if item.Type != "quiz" {
		fmt.Fprintf(os.Stderr, "%s is not a quiz; use: uni grade %s\n", item.ID, args[0])
		return 2
	}
	quiz, err := loadQuiz(root, ref.Dir, item.Path)
	if err != nil {
		fmt.Fprintln(os.Stderr, "error:", err)
		return 1
	}
	now := uint64(time.Now().UnixMicro())
	randomizer := rand.New(rand.NewPCG(now, now))
	score, err := administerQuiz(quiz, randomizer, os.Stdin, os.Stdout)
	if err != nil {
		fmt.Fprintln(os.Stderr, "error:", err)
		return 1
	}
	if dry {
		fmt.Println("(dry run: not recorded)")
		return 0
	}
	record, err := recordAttempt(root, item, ref.ID, score, curriculum.PassBar, time.Now())
	if err != nil {
		fmt.Fprintln(os.Stderr, "error:", err)
		return 1
	}
	reportRecord(record)
	return 0
}

func reportRecord(record Record) {
	verdict := "not yet passing"
	if record.Passed {
		verdict = "passed"
	}
	fmt.Printf("Recorded: best %.0f%% over %d attempt(s) — %s\n",
		record.BestScore*100, record.Attempts, verdict)
}

func runNext(root string, curriculum Curriculum) int {
	for _, ref := range curriculum.Courses {
		course, authored, err := loadCourse(root, ref)
		if err != nil {
			fmt.Fprintln(os.Stderr, "error:", err)
			return 1
		}
		if !authored {
			fmt.Printf("Next: %s — %s (content not yet authored; ask your professor)\n", ref.ID, ref.Title)
			return 0
		}
		records, err := loadCourseRecords(root, ref.ID)
		if err != nil {
			fmt.Fprintln(os.Stderr, "error:", err)
			return 1
		}
		for _, item := range course.Items {
			record, found := records[item.ID]
			if found && record.Passed {
				continue
			}
			action := "uni grade"
			if item.Type == "quiz" {
				action = "uni quiz"
			}
			fmt.Printf("Next: %s — %s: %s (%s)\n", ref.ID, ref.Title, item.Title, item.ID)
			fmt.Printf("  materials: %s\n", course.itemLocation(ref, item))
			fmt.Printf("  then run:  %s %s/%s\n", action, ref.ID, item.ID)
			return 0
		}
		if !course.ContentComplete {
			fmt.Printf("Next: %s — %s: everything authored so far is passed; ask your professor for more content\n", ref.ID, ref.Title)
			return 0
		}
	}
	fmt.Println("Degree complete. Congratulations, graduate.")
	return 0
}

func (this Course) itemLocation(ref CourseRef, item Item) string {
	return ref.Dir + "/" + item.Path
}

func runHash(args []string) int {
	if len(args) != 2 {
		fmt.Fprintln(os.Stderr, "usage: uni hash <salt> <answer>")
		return 2
	}
	fmt.Println(hashAnswer(args[0], args[1]))
	return 0
}

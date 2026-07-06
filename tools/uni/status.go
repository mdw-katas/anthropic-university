package main

import (
	"fmt"
	"io"
	"strings"
)

// letterGrade maps a 0..1 score to a letter and 4.0-scale grade points.
func letterGrade(score float64) (letter string, points float64) {
	scale := []struct {
		Floor  float64
		Letter string
		Points float64
	}{
		{Floor: 0.93, Letter: "A", Points: 4.0},
		{Floor: 0.90, Letter: "A-", Points: 3.7},
		{Floor: 0.87, Letter: "B+", Points: 3.3},
		{Floor: 0.83, Letter: "B", Points: 3.0},
		{Floor: 0.80, Letter: "B-", Points: 2.7},
		{Floor: 0.77, Letter: "C+", Points: 2.3},
		{Floor: 0.73, Letter: "C", Points: 2.0},
		{Floor: 0.70, Letter: "C-", Points: 1.7},
		{Floor: 0.67, Letter: "D+", Points: 1.3},
		{Floor: 0.63, Letter: "D", Points: 1.0},
		{Floor: 0.60, Letter: "D-", Points: 0.7},
	}
	for _, grade := range scale {
		if score >= grade.Floor {
			return grade.Letter, grade.Points
		}
	}
	return "F", 0.0
}

// standing is the computed academic position within one course.
type standing struct {
	Ref         CourseRef
	Authored    bool
	TotalItems  int
	PassedItems int
	Attempted   int
	Score       float64
	Complete    bool
}

// computeStanding produces a course grade as the weighted average of
// component scores, where each component is the mean best-score of its
// items (unattempted items count as zero). Components with no authored
// items are excluded and the remaining weights renormalized, so a
// partially authored course is graded only on what exists.
func computeStanding(ref CourseRef, course Course, records map[string]Record) (result standing) {
	result.Ref = ref
	result.Authored = true
	result.TotalItems = len(course.Items)
	weightedSum, weightTotal := 0.0, 0.0
	for _, component := range course.Components {
		itemCount, scoreSum := 0, 0.0
		for _, item := range course.Items {
			if item.Type != component.Type {
				continue
			}
			itemCount++
			if record, found := records[item.ID]; found {
				scoreSum += record.BestScore
			}
		}
		if itemCount == 0 {
			continue
		}
		weightedSum += component.Weight * (scoreSum / float64(itemCount))
		weightTotal += component.Weight
	}
	if weightTotal > 0 {
		result.Score = weightedSum / weightTotal
	}
	for _, item := range course.Items {
		record, found := records[item.ID]
		if !found {
			continue
		}
		result.Attempted++
		if record.Passed {
			result.PassedItems++
		}
	}
	result.Complete = course.ContentComplete &&
		result.TotalItems > 0 &&
		result.PassedItems == result.TotalItems
	return result
}

func progressBar(fraction float64, width int) string {
	filled := int(fraction*float64(width) + 0.5)
	filled = min(max(filled, 0), width)
	return "[" + strings.Repeat("#", filled) + strings.Repeat("-", width-filled) + "]"
}

func (this standing) describe() string {
	switch {
	case !this.Authored:
		return "not yet authored"
	case this.Complete:
		letter, _ := letterGrade(this.Score)
		return fmt.Sprintf("complete: %s", letter)
	case this.Attempted == 0:
		return "not started"
	default:
		letter, _ := letterGrade(this.Score)
		return fmt.Sprintf("in progress: %s so far", letter)
	}
}

func renderDegreeStatus(out io.Writer, curriculum Curriculum, standings []standing) {
	fmt.Fprintf(out, "\n%s\n\n", curriculum.Degree)
	earnedCredits, totalCredits := 0, 0
	gpaPoints, gpaCredits := 0.0, 0
	for _, course := range standings {
		totalCredits += course.Ref.Credits
		if course.Complete {
			earnedCredits += course.Ref.Credits
			_, points := letterGrade(course.Score)
			gpaPoints += points * float64(course.Ref.Credits)
			gpaCredits += course.Ref.Credits
		}
	}
	for _, course := range standings {
		completion := 0.0
		if course.TotalItems > 0 {
			completion = float64(course.PassedItems) / float64(course.TotalItems)
		}
		fmt.Fprintf(out, "  %-4s %-40s %s %3.0f%%  %s\n",
			course.Ref.ID, course.Ref.Title,
			progressBar(completion, 10), completion*100,
			course.describe())
	}
	gpa := "—"
	if gpaCredits > 0 {
		gpa = fmt.Sprintf("%.2f", gpaPoints/float64(gpaCredits))
	}
	fmt.Fprintf(out, "\nCredits earned: %d/%d    GPA: %s\n", earnedCredits, totalCredits, gpa)
}

func renderCourseStatus(out io.Writer, ref CourseRef, course Course, records map[string]Record) {
	position := computeStanding(ref, course, records)
	fmt.Fprintf(out, "\n%s — %s\n\n", ref.ID, ref.Title)
	for _, item := range course.Items {
		record, found := records[item.ID]
		state := "not attempted"
		if found {
			mark := "✗"
			if record.Passed {
				mark = "✓"
			}
			state = fmt.Sprintf("%s %3.0f%% (best of %d attempt(s))", mark, record.BestScore*100, record.Attempts)
		}
		fmt.Fprintf(out, "  %-12s %-11s %-34s %s\n", item.ID, item.Type, item.Title, state)
	}
	letter, _ := letterGrade(position.Score)
	fmt.Fprintf(out, "\nCourse grade so far: %.0f%% (%s)    Items passed: %d/%d\n",
		position.Score*100, letter, position.PassedItems, position.TotalItems)
	if !course.ContentComplete {
		fmt.Fprintln(out, "Note: course content is still being authored; more items will appear.")
	}
}

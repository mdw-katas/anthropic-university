package main

import (
	"encoding/json"
	"fmt"
	"os"
	"path/filepath"
)

// Curriculum is the machine-readable degree map at the repository root.
type Curriculum struct {
	Degree  string      `json:"degree"`
	PassBar float64     `json:"pass_bar"`
	Courses []CourseRef `json:"courses"`
}

// CourseRef is one row of the degree map.
type CourseRef struct {
	ID            string   `json:"id"`
	Dir           string   `json:"dir"`
	Title         string   `json:"title"`
	Credits       int      `json:"credits"`
	Prerequisites []string `json:"prerequisites"`
}

// Course is the per-course manifest (course.json) listing gradable items.
type Course struct {
	ID              string      `json:"id"`
	Title           string      `json:"title"`
	ContentComplete bool        `json:"content_complete"`
	Components      []Component `json:"components"`
	Items           []Item      `json:"items"`
}

// Component assigns a grade weight to an item type (assignment, quiz, ...).
type Component struct {
	Type   string  `json:"type"`
	Weight float64 `json:"weight"`
}

// Item is one gradable unit of a course.
type Item struct {
	ID       string `json:"id"`
	Type     string `json:"type"`
	Title    string `json:"title"`
	Path     string `json:"path"`
	Runner   string `json:"runner,omitempty"`
	TestsDir string `json:"tests_dir,omitempty"`
}

func findRoot() (root string, err error) {
	dir, err := os.Getwd()
	if err != nil {
		return "", err
	}
	for {
		candidate := filepath.Join(dir, "curriculum.json")
		if _, statErr := os.Stat(candidate); statErr == nil {
			return dir, nil
		}
		parent := filepath.Dir(dir)
		if parent == dir {
			return "", fmt.Errorf("curriculum.json not found in any parent of the working directory")
		}
		dir = parent
	}
}

func loadCurriculum(root string) (curriculum Curriculum, err error) {
	data, err := os.ReadFile(filepath.Join(root, "curriculum.json"))
	if err != nil {
		return Curriculum{}, err
	}
	err = json.Unmarshal(data, &curriculum)
	if err != nil {
		return Curriculum{}, fmt.Errorf("parsing curriculum.json: %w", err)
	}
	return curriculum, nil
}

func (this Curriculum) findCourse(id string) (ref CourseRef, found bool) {
	for _, course := range this.Courses {
		if course.ID == id {
			return course, true
		}
	}
	return CourseRef{}, false
}

func loadCourse(root string, ref CourseRef) (course Course, authored bool, err error) {
	path := filepath.Join(root, ref.Dir, "course.json")
	data, err := os.ReadFile(path)
	if os.IsNotExist(err) {
		return Course{}, false, nil
	}
	if err != nil {
		return Course{}, false, err
	}
	err = json.Unmarshal(data, &course)
	if err != nil {
		return Course{}, false, fmt.Errorf("parsing %s: %w", path, err)
	}
	return course, true, nil
}

func (this Course) findItem(id string) (item Item, found bool) {
	for _, candidate := range this.Items {
		if candidate.ID == id {
			return candidate, true
		}
	}
	return Item{}, false
}

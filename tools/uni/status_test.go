package main

import (
	"strings"
	"testing"
)

func TestLetterGrade(t *testing.T) {
	cases := []struct {
		Score  float64
		Letter string
		Points float64
	}{
		{Score: 1.00, Letter: "A", Points: 4.0},
		{Score: 0.93, Letter: "A", Points: 4.0},
		{Score: 0.92, Letter: "A-", Points: 3.7},
		{Score: 0.87, Letter: "B+", Points: 3.3},
		{Score: 0.85, Letter: "B", Points: 3.0},
		{Score: 0.80, Letter: "B-", Points: 2.7},
		{Score: 0.78, Letter: "C+", Points: 2.3},
		{Score: 0.75, Letter: "C", Points: 2.0},
		{Score: 0.70, Letter: "C-", Points: 1.7},
		{Score: 0.68, Letter: "D+", Points: 1.3},
		{Score: 0.65, Letter: "D", Points: 1.0},
		{Score: 0.60, Letter: "D-", Points: 0.7},
		{Score: 0.59, Letter: "F", Points: 0.0},
		{Score: 0.00, Letter: "F", Points: 0.0},
	}
	for _, test := range cases {
		letter, points := letterGrade(test.Score)
		if letter != test.Letter || points != test.Points {
			t.Errorf("letterGrade(%.2f) = %s/%.1f, want %s/%.1f",
				test.Score, letter, points, test.Letter, test.Points)
		}
	}
}

func fixtureCourse() Course {
	return Course{
		ID:              "101",
		ContentComplete: false,
		Components: []Component{
			{Type: "exploration", Weight: 0.10},
			{Type: "quiz", Weight: 0.20},
			{Type: "assignment", Weight: 0.45},
			{Type: "final", Weight: 0.25},
		},
		Items: []Item{
			{ID: "explore-01", Type: "exploration"},
			{ID: "q1", Type: "quiz"},
			{ID: "a1", Type: "assignment"},
		},
	}
}

func TestComputeStandingRenormalizesMissingComponents(t *testing.T) {
	// No "final" item is authored, so the final's 0.25 weight must be
	// excluded: perfect scores on everything else should yield 1.0.
	records := map[string]Record{
		"explore-01": {BestScore: 1.0, Passed: true},
		"q1":         {BestScore: 1.0, Passed: true},
		"a1":         {BestScore: 1.0, Passed: true},
	}
	result := computeStanding(CourseRef{ID: "101"}, fixtureCourse(), records)
	if result.Score < 0.999 || result.Score > 1.001 {
		t.Errorf("Score = %.4f, want 1.0", result.Score)
	}
	if result.PassedItems != 3 || result.TotalItems != 3 {
		t.Errorf("PassedItems/TotalItems = %d/%d, want 3/3", result.PassedItems, result.TotalItems)
	}
	if result.Complete {
		t.Error("course should not be Complete while content_complete is false")
	}
}

func TestComputeStandingCountsUnattemptedAsZero(t *testing.T) {
	// Only the assignment attempted, at 100%. Weighted: (0.45*1.0) / 0.75.
	records := map[string]Record{
		"a1": {BestScore: 1.0, Passed: true},
	}
	result := computeStanding(CourseRef{ID: "101"}, fixtureCourse(), records)
	expected := 0.45 / 0.75
	if result.Score < expected-0.001 || result.Score > expected+0.001 {
		t.Errorf("Score = %.4f, want %.4f", result.Score, expected)
	}
	if result.Attempted != 1 {
		t.Errorf("Attempted = %d, want 1", result.Attempted)
	}
}

func TestComputeStandingCompleteCourse(t *testing.T) {
	course := fixtureCourse()
	course.ContentComplete = true
	records := map[string]Record{
		"explore-01": {BestScore: 0.9, Passed: true},
		"q1":         {BestScore: 0.85, Passed: true},
		"a1":         {BestScore: 0.95, Passed: true},
	}
	result := computeStanding(CourseRef{ID: "101"}, course, records)
	if !result.Complete {
		t.Error("all items passed and content complete: course should be Complete")
	}
}

func TestProgressBar(t *testing.T) {
	if bar := progressBar(0.5, 10); bar != "[#####-----]" {
		t.Errorf("progressBar(0.5) = %s", bar)
	}
	if bar := progressBar(0, 10); bar != "[----------]" {
		t.Errorf("progressBar(0) = %s", bar)
	}
	if bar := progressBar(1.2, 10); !strings.HasPrefix(bar, "[##########") {
		t.Errorf("progressBar(1.2) = %s", bar)
	}
}

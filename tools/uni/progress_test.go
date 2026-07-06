package main

import (
	"testing"
	"time"
)

func TestRecordAttemptKeepsBestScore(t *testing.T) {
	root := t.TempDir()
	item := Item{ID: "a1", Type: "assignment"}
	now := time.Date(2026, 7, 5, 12, 0, 0, 0, time.UTC)
	first, err := recordAttempt(root, item, "101", 0.5, 0.8, now)
	if err != nil {
		t.Fatal(err)
	}
	if first.Attempts != 1 || first.BestScore != 0.5 || first.Passed {
		t.Errorf("first attempt = %+v, want attempts=1 best=0.5 passed=false", first)
	}
	second, err := recordAttempt(root, item, "101", 0.3, 0.8, now)
	if err != nil {
		t.Fatal(err)
	}
	if second.Attempts != 2 || second.BestScore != 0.5 || second.LastScore != 0.3 {
		t.Errorf("second attempt = %+v, want attempts=2 best=0.5 last=0.3", second)
	}
	third, err := recordAttempt(root, item, "101", 0.9, 0.8, now)
	if err != nil {
		t.Fatal(err)
	}
	if third.Attempts != 3 || third.BestScore != 0.9 || !third.Passed {
		t.Errorf("third attempt = %+v, want attempts=3 best=0.9 passed=true", third)
	}
	loaded, found, err := loadRecord(root, "101", "a1")
	if err != nil || !found {
		t.Fatalf("loadRecord: found=%v err=%v", found, err)
	}
	if loaded != third {
		t.Errorf("persisted record %+v != returned record %+v", loaded, third)
	}
}

func TestLoadCourseRecordsEmptyWhenNoneExist(t *testing.T) {
	records, err := loadCourseRecords(t.TempDir(), "101")
	if err != nil {
		t.Fatal(err)
	}
	if len(records) != 0 {
		t.Errorf("expected no records, got %d", len(records))
	}
}

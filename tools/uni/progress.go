package main

import (
	"encoding/json"
	"os"
	"path/filepath"
	"time"
)

// Record is the committed result for one item; only the best score persists
// as the grade (mastery model), while attempts and the last score are kept
// for the historical record.
type Record struct {
	Course    string  `json:"course"`
	Item      string  `json:"item"`
	Type      string  `json:"type"`
	BestScore float64 `json:"best_score"`
	LastScore float64 `json:"last_score"`
	Attempts  int     `json:"attempts"`
	Passed    bool    `json:"passed"`
	Updated   string  `json:"updated"`
}

func recordPath(root, courseID, itemID string) string {
	return filepath.Join(root, "progress", courseID, itemID+".json")
}

func loadRecord(root, courseID, itemID string) (record Record, found bool, err error) {
	data, err := os.ReadFile(recordPath(root, courseID, itemID))
	if os.IsNotExist(err) {
		return Record{}, false, nil
	}
	if err != nil {
		return Record{}, false, err
	}
	err = json.Unmarshal(data, &record)
	if err != nil {
		return Record{}, false, err
	}
	return record, true, nil
}

func loadCourseRecords(root, courseID string) (records map[string]Record, err error) {
	records = map[string]Record{}
	entries, err := os.ReadDir(filepath.Join(root, "progress", courseID))
	if os.IsNotExist(err) {
		return records, nil
	}
	if err != nil {
		return nil, err
	}
	for _, entry := range entries {
		if entry.IsDir() || filepath.Ext(entry.Name()) != ".json" {
			continue
		}
		itemID := entry.Name()[:len(entry.Name())-len(".json")]
		record, found, loadErr := loadRecord(root, courseID, itemID)
		if loadErr != nil {
			return nil, loadErr
		}
		if found {
			records[itemID] = record
		}
	}
	return records, nil
}

func recordAttempt(root string, item Item, courseID string, score, passBar float64, now time.Time) (record Record, err error) {
	record, _, err = loadRecord(root, courseID, item.ID)
	if err != nil {
		return Record{}, err
	}
	record.Course = courseID
	record.Item = item.ID
	record.Type = item.Type
	record.Attempts++
	record.LastScore = score
	record.BestScore = max(record.BestScore, score)
	record.Passed = record.BestScore >= passBar
	record.Updated = now.Format(time.RFC3339)
	path := recordPath(root, courseID, item.ID)
	err = os.MkdirAll(filepath.Dir(path), 0o755)
	if err != nil {
		return Record{}, err
	}
	data, err := json.MarshalIndent(record, "", "  ")
	if err != nil {
		return Record{}, err
	}
	err = os.WriteFile(path, append(data, '\n'), 0o644)
	if err != nil {
		return Record{}, err
	}
	return record, nil
}

package main

import (
	"fmt"
	"os/exec"
	"path/filepath"
	"regexp"
	"strconv"
)

// suiteResult summarizes one run of an item's test suite.
type suiteResult struct {
	Ran     int
	Failed  int
	Errored int
	Skipped int
	Output  string
}

func (this suiteResult) Score() float64 {
	counted := this.Ran - this.Skipped
	if counted <= 0 {
		return 0
	}
	passed := counted - this.Failed - this.Errored
	if passed < 0 {
		passed = 0
	}
	return float64(passed) / float64(counted)
}

var (
	ranPattern     = regexp.MustCompile(`Ran (\d+) tests?`)
	failurePattern = regexp.MustCompile(`failures=(\d+)`)
	errorPattern   = regexp.MustCompile(`errors=(\d+)`)
	skipPattern    = regexp.MustCompile(`skipped=(\d+)`)
)

func parseUnittestOutput(output string) (result suiteResult) {
	result.Output = output
	result.Ran = extractCount(ranPattern, output)
	result.Failed = extractCount(failurePattern, output)
	result.Errored = extractCount(errorPattern, output)
	result.Skipped = extractCount(skipPattern, output)
	return result
}

func extractCount(pattern *regexp.Regexp, output string) int {
	match := pattern.FindStringSubmatch(output)
	if match == nil {
		return 0
	}
	count, err := strconv.Atoi(match[1])
	if err != nil {
		return 0
	}
	return count
}

func runSuite(root string, courseDir string, item Item) (result suiteResult, err error) {
	testsDir := item.TestsDir
	if testsDir == "" {
		testsDir = "tests"
	}
	command := exec.Command("python3", "-m", "unittest", "discover",
		"-v",
		"-s", testsDir,
		"-t", testsDir,
		"-p", "test_*.py",
	)
	command.Dir = filepath.Join(root, courseDir, item.Path)
	output, runErr := command.CombinedOutput()
	if len(output) == 0 && runErr != nil {
		return suiteResult{}, fmt.Errorf("running test suite: %w", runErr)
	}
	return parseUnittestOutput(string(output)), nil
}

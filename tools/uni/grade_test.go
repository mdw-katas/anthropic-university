package main

import "testing"

func TestParseUnittestOutputAllPassing(t *testing.T) {
	output := `test_gcd_basic (test_algorithms.TestGCD.test_gcd_basic) ... ok

----------------------------------------------------------------------
Ran 5 tests in 0.001s

OK
`
	result := parseUnittestOutput(output)
	if result.Ran != 5 || result.Failed != 0 || result.Errored != 0 {
		t.Errorf("parsed %+v, want Ran=5 Failed=0 Errored=0", result)
	}
	if result.Score() != 1.0 {
		t.Errorf("Score() = %.2f, want 1.0", result.Score())
	}
}

func TestParseUnittestOutputWithFailuresAndErrors(t *testing.T) {
	output := `----------------------------------------------------------------------
Ran 10 tests in 0.004s

FAILED (failures=2, errors=3)
`
	result := parseUnittestOutput(output)
	if result.Ran != 10 || result.Failed != 2 || result.Errored != 3 {
		t.Errorf("parsed %+v, want Ran=10 Failed=2 Errored=3", result)
	}
	if result.Score() != 0.5 {
		t.Errorf("Score() = %.2f, want 0.5", result.Score())
	}
}

func TestParseUnittestOutputWithSkips(t *testing.T) {
	output := `Ran 8 tests in 0.002s

FAILED (failures=1, skipped=2)
`
	result := parseUnittestOutput(output)
	if result.Skipped != 2 {
		t.Errorf("Skipped = %d, want 2", result.Skipped)
	}
	// 8 ran - 2 skipped = 6 counted; 5 passed.
	expected := 5.0 / 6.0
	if result.Score() < expected-0.001 || result.Score() > expected+0.001 {
		t.Errorf("Score() = %.4f, want %.4f", result.Score(), expected)
	}
}

func TestParseUnittestOutputSingleTest(t *testing.T) {
	output := `Ran 1 test in 0.000s

OK
`
	result := parseUnittestOutput(output)
	if result.Ran != 1 {
		t.Errorf("Ran = %d, want 1", result.Ran)
	}
}

func TestParseUnittestOutputGarbage(t *testing.T) {
	result := parseUnittestOutput("python3: command exploded")
	if result.Score() != 0 {
		t.Errorf("Score() on garbage = %.2f, want 0", result.Score())
	}
}

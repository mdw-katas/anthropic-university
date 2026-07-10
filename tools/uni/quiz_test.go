package main

import (
	"math"
	"math/rand/v2"
	"strings"
	"testing"
)

func TestHashAnswerNormalizes(t *testing.T) {
	base := hashAnswer("salt1", "b")
	if hashAnswer("salt1", " B \n") != base {
		t.Error("hash should ignore case and surrounding whitespace")
	}
	if hashAnswer("salt2", "b") == base {
		t.Error("different salts must produce different hashes")
	}
	if hashAnswer("salt1", "c") == base {
		t.Error("different answers must produce different hashes")
	}
}

func fixtureQuiz() Quiz {
	return Quiz{
		ID:    "q0",
		Title: "Fixture Quiz",
		Questions: []Question{
			{
				ID:         "q0-1",
				Prompt:     "Pick a.",
				Choices:    []string{"right", "wrong"},
				Salt:       "s1",
				AnswerHash: hashAnswer("s1", "a"),
			},
			{
				ID:         "q0-2",
				Prompt:     "Pick b.",
				Choices:    []string{"wrong", "right"},
				Salt:       "s2",
				AnswerHash: hashAnswer("s2", "b"),
			},
		},
	}
}

func TestAdministerQuizPerfectScore(t *testing.T) {
	var out strings.Builder
	score, err := administerQuiz(fixtureQuiz(), noShuffleRand, strings.NewReader("a\nb\n"), &out)
	if err != nil {
		t.Fatal(err)
	}
	if score != 1.0 {
		t.Errorf("score = %.2f, want 1.0", score)
	}
	if !strings.Contains(out.String(), "2/2") {
		t.Errorf("output should report 2/2, got:\n%s", out.String())
	}
}

func TestAdministerQuizHalfScore(t *testing.T) {
	var out strings.Builder
	score, err := administerQuiz(fixtureQuiz(), noShuffleRand, strings.NewReader("a\na\n"), &out)
	if err != nil {
		t.Fatal(err)
	}
	if score != 0.5 {
		t.Errorf("score = %.2f, want 0.5", score)
	}
}

func TestAdministerQuizRejectsInvalidChoiceThenAccepts(t *testing.T) {
	var out strings.Builder
	score, err := administerQuiz(fixtureQuiz(), noShuffleRand, strings.NewReader("z\na\nb\n"), &out)
	if err != nil {
		t.Fatal(err)
	}
	if score != 1.0 {
		t.Errorf("score = %.2f, want 1.0 after invalid answer retried", score)
	}
	if !strings.Contains(out.String(), "please answer a-b") {
		t.Errorf("output should coach valid range, got:\n%s", out.String())
	}
}

func TestAdministerQuizErrorsOnTruncatedInput(t *testing.T) {
	var out strings.Builder
	_, err := administerQuiz(fixtureQuiz(), noShuffleRand, strings.NewReader("a\n"), &out)
	if err == nil {
		t.Error("expected an error when input ends before the quiz does")
	}
}

type noShuffleSource struct{}

func (noShuffleSource) Uint64() uint64 { return math.MaxUint64 }

var noShuffleRand = rand.New(noShuffleSource{})

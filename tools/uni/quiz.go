package main

import (
	"bufio"
	"crypto/sha256"
	"encoding/hex"
	"encoding/json"
	"fmt"
	"io"
	"math/rand/v2"
	"os"
	"path/filepath"
	"slices"
	"strings"
)

// Quiz is an interactive multiple-choice assessment. Correct answers are
// stored as salted SHA-256 hashes so reading the file doesn't spoil it.
type Quiz struct {
	ID        string     `json:"id"`
	Title     string     `json:"title"`
	Questions []Question `json:"questions"`
}

// Question holds one prompt; Choices are displayed as a), b), c), ...
type Question struct {
	ID         string   `json:"id"`
	Prompt     string   `json:"prompt"`
	Choices    []string `json:"choices"`
	Salt       string   `json:"salt"`
	AnswerHash string   `json:"answer_hash"`
}

func hashAnswer(salt, answer string) string {
	normalized := strings.ToLower(strings.TrimSpace(answer))
	sum := sha256.Sum256([]byte(salt + ":" + normalized))
	return hex.EncodeToString(sum[:])
}

func (this Question) isCorrect(answer string) bool {
	return hashAnswer(this.Salt, answer) == this.AnswerHash
}

func loadQuiz(root, courseDir, quizPath string) (quiz Quiz, err error) {
	data, err := os.ReadFile(filepath.Join(root, courseDir, quizPath))
	if err != nil {
		return Quiz{}, err
	}
	err = json.Unmarshal(data, &quiz)
	if err != nil {
		return Quiz{}, fmt.Errorf("parsing quiz %s: %w", quizPath, err)
	}
	return quiz, nil
}

func administerQuiz(quiz Quiz, randomizer *rand.Rand, in io.Reader, out io.Writer) (score float64, err error) {
	reader := bufio.NewReader(in)
	correct := 0
	fmt.Fprintf(out, "\n%s (%d questions)\n\n", quiz.Title, len(quiz.Questions))
	for number, question := range quiz.Questions {
		fmt.Fprintf(out, "%d. %s\n", number+1, question.Prompt)
		choices := slices.Clone(question.Choices)
		randomizer.Shuffle(len(choices), func(i, j int) {
			choices[i], choices[j] = choices[j], choices[i]
		})
		mapping := make(map[string]string)
		for originalIndex, original := range question.Choices {
			randomizedIndex := slices.Index(choices, original)
			originalLetter := fmt.Sprintf("%c", 'a'+originalIndex)
			randomizedLetter := fmt.Sprintf("%c", 'a'+randomizedIndex)
			mapping[randomizedLetter] = originalLetter
		}
		for choice, text := range choices {
			fmt.Fprintf(out, "   %c) %s\n", 'a'+choice, text)
		}
		answer, readErr := promptForChoice(reader, out, len(choices))
		if readErr != nil {
			return 0, readErr
		}
		if question.isCorrect(mapping[answer]) {
			correct++
			fmt.Fprintln(out, "   ✓ correct")
		} else {
			fmt.Fprintln(out, "   ✗ incorrect")
		}
		fmt.Fprintln(out)
	}
	if len(quiz.Questions) == 0 {
		return 0, nil
	}
	score = float64(correct) / float64(len(quiz.Questions))
	fmt.Fprintf(out, "Result: %d/%d (%.0f%%)\n", correct, len(quiz.Questions), score*100)
	return score, nil
}

func promptForChoice(reader *bufio.Reader, out io.Writer, choiceCount int) (answer string, err error) {
	for {
		fmt.Fprint(out, "   your answer: ")
		line, readErr := reader.ReadString('\n')
		if readErr != nil && line == "" {
			return "", fmt.Errorf("reading answer: %w", readErr)
		}
		answer = strings.ToLower(strings.TrimSpace(line))
		if isValidChoice(answer, choiceCount) {
			return answer, nil
		}
		fmt.Fprintf(out, "   please answer a-%c\n", 'a'+choiceCount-1)
		if readErr != nil {
			return "", fmt.Errorf("reading answer: %w", readErr)
		}
	}
}

func isValidChoice(answer string, choiceCount int) bool {
	if len(answer) != 1 {
		return false
	}
	letter := answer[0]
	return letter >= 'a' && int(letter-'a') < choiceCount
}

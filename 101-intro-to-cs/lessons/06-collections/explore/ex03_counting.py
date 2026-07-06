"""Exploration: the dict counting idiom and set deduplication.

Predict, run, then: uni grade 101/explore-06
"""

TEXT = "the quick brown fox jumps over the lazy dog and the cat"

PREDICT_COUNT_THE = None     # how many times "the" appears
PREDICT_UNIQUE_WORDS = None  # how many DISTINCT words in TEXT


def word_counts(text):
    counts = {}
    for word in text.split():
        counts[word] = counts.get(word, 0) + 1
    return counts


if __name__ == "__main__":
    counts = word_counts(TEXT)
    print(f"counts['the']    = {counts['the']}")
    print(f"distinct words   = {len(set(TEXT.split()))}")

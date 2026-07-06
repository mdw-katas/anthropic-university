"""Assignment a4: word statistics. The test suite is the specification."""


def normalize_words(text):
    """Return the words of text: lowercased, split on whitespace, with
    leading/trailing punctuation stripped from each token.

    Tokens that were entirely punctuation disappear.
    normalize_words("Stop! Go.") == ["stop", "go"]
    """
    raise NotImplementedError


def word_frequencies(text):
    """Return {word: count} over normalize_words(text)."""
    raise NotImplementedError


def top_n(frequencies, n):
    """Return the n most frequent (word, count) pairs, highest count first,
    ties broken alphabetically. Fewer than n words? Return them all.
    """
    raise NotImplementedError


def bigrams(words):
    """Return the list of adjacent pairs as tuples.

    bigrams(["a", "b", "c"]) == [("a", "b"), ("b", "c")]; bigrams([]) == [].
    """
    raise NotImplementedError


def vocabulary_richness(text):
    """Return distinct-word count divided by total-word count, as a float.

    An empty text (no words) has richness 0.0.
    """
    raise NotImplementedError

"""The executable specification for assignment a4."""
import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "starter"))

import word_stats


class TestNormalizeWords(unittest.TestCase):
    def test_lowercase_and_split(self):
        self.assertEqual(word_stats.normalize_words("The Quick Fox"),
                         ["the", "quick", "fox"])

    def test_strips_edge_punctuation(self):
        self.assertEqual(word_stats.normalize_words("Stop! Go. Now?"),
                         ["stop", "go", "now"])

    def test_keeps_interior_punctuation(self):
        self.assertEqual(word_stats.normalize_words("don't stop"),
                         ["don't", "stop"])

    def test_pure_punctuation_vanishes(self):
        self.assertEqual(word_stats.normalize_words("wait -- what"),
                         ["wait", "what"])

    def test_empty(self):
        self.assertEqual(word_stats.normalize_words(""), [])
        self.assertEqual(word_stats.normalize_words("   "), [])


class TestWordFrequencies(unittest.TestCase):
    def test_counts(self):
        frequencies = word_stats.word_frequencies("the cat and the dog and the bird")
        self.assertEqual(frequencies["the"], 3)
        self.assertEqual(frequencies["and"], 2)
        self.assertEqual(frequencies["cat"], 1)

    def test_normalization_applies(self):
        frequencies = word_stats.word_frequencies("Dog dog DOG!")
        self.assertEqual(frequencies, {"dog": 3})


class TestTopN(unittest.TestCase):
    def test_ordering(self):
        frequencies = {"pear": 3, "apple": 5, "plum": 3, "fig": 1}
        self.assertEqual(word_stats.top_n(frequencies, 3),
                         [("apple", 5), ("pear", 3), ("plum", 3)])

    def test_ties_break_alphabetically(self):
        frequencies = {"zed": 2, "ant": 2}
        self.assertEqual(word_stats.top_n(frequencies, 2),
                         [("ant", 2), ("zed", 2)])

    def test_asking_for_too_many(self):
        self.assertEqual(word_stats.top_n({"only": 1}, 10), [("only", 1)])

    def test_empty(self):
        self.assertEqual(word_stats.top_n({}, 5), [])


class TestBigrams(unittest.TestCase):
    def test_pairs(self):
        self.assertEqual(word_stats.bigrams(["a", "b", "c"]),
                         [("a", "b"), ("b", "c")])

    def test_short_inputs(self):
        self.assertEqual(word_stats.bigrams(["solo"]), [])
        self.assertEqual(word_stats.bigrams([]), [])


class TestVocabularyRichness(unittest.TestCase):
    def test_all_distinct(self):
        self.assertAlmostEqual(word_stats.vocabulary_richness("one two three"), 1.0)

    def test_repetition_lowers_richness(self):
        self.assertAlmostEqual(word_stats.vocabulary_richness("yes yes yes yes"), 0.25)

    def test_mixed(self):
        self.assertAlmostEqual(
            word_stats.vocabulary_richness("the cat the dog"), 0.75)

    def test_empty_is_zero(self):
        self.assertEqual(word_stats.vocabulary_richness(""), 0.0)


if __name__ == "__main__":
    unittest.main()

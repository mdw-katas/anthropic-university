"""Self-checks for the Lesson 6 explorations: uni grade 101/explore-06"""
import unittest

import ex01_aliasing
import ex02_tuples
import ex03_counting


class TestAliasing(unittest.TestCase):
    def test_shared_list_mutated(self):
        shared, _ = ex01_aliasing.main()
        self.assertEqual(ex01_aliasing.PREDICT_SHARED_AFTER, shared)

    def test_copied_list_untouched(self):
        _, copied = ex01_aliasing.main()
        self.assertEqual(ex01_aliasing.PREDICT_COPIED_AFTER, copied)


class TestTuples(unittest.TestCase):
    def test_list_inside_tuple(self):
        self.assertEqual(ex02_tuples.PREDICT_LIST_INSIDE, ex02_tuples.mutate_inside())

    def test_replacement_raises(self):
        self.assertEqual(ex02_tuples.PREDICT_REPLACE_RAISES, ex02_tuples.try_replace())


class TestCounting(unittest.TestCase):
    def test_count_the(self):
        counts = ex03_counting.word_counts(ex03_counting.TEXT)
        self.assertEqual(ex03_counting.PREDICT_COUNT_THE, counts["the"])

    def test_unique_words(self):
        self.assertEqual(ex03_counting.PREDICT_UNIQUE_WORDS,
                         len(set(ex03_counting.TEXT.split())))


if __name__ == "__main__":
    unittest.main()

"""Self-checks for the Lesson 2 explorations: uni grade 102/explore-02"""
import unittest

import ex01_duck_typing
import ex02_two_representations
import ex03_leaky_roster


class TestDuckTyping(unittest.TestCase):
    def test_list_drain(self):
        self.assertEqual(ex01_duck_typing.PREDICT_LIST_DRAIN,
                         ex01_duck_typing.drain([1, 2, 3]))

    def test_dict_failure(self):
        self.assertEqual(ex01_duck_typing.PREDICT_DICT_FAILURE,
                         ex01_duck_typing.dict_failure_name())


class TestTwoRepresentations(unittest.TestCase):
    def test_outputs_match(self):
        module = ex02_two_representations
        via_array = module.reverse_via(module.ArrayStack(), [1, 2, 3])
        via_linked = module.reverse_via(module.LinkedStack(), [1, 2, 3])
        self.assertEqual(module.PREDICT_OUTPUTS_MATCH, via_array == via_linked)

    def test_array_internal_order(self):
        module = ex02_two_representations
        self.assertEqual(module.PREDICT_ARRAY_INTERNAL,
                         module.array_internal_after([1, 2, 3]))


class TestLeakyRoster(unittest.TestCase):
    def test_leaky_roster_is_corrupted(self):
        module = ex03_leaky_roster
        self.assertEqual(module.PREDICT_LEAKY_AFTER,
                         module.roster_after(module.LeakyRoster))

    def test_sealed_roster_is_safe(self):
        module = ex03_leaky_roster
        self.assertEqual(module.PREDICT_SEALED_AFTER,
                         module.roster_after(module.SealedRoster))


if __name__ == "__main__":
    unittest.main()

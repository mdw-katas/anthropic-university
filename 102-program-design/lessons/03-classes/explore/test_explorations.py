"""Self-checks for the Lesson 3 explorations: uni grade 102/explore-03"""
import unittest

import ex01_class_vs_instance
import ex02_eq_and_hash
import ex03_name_mangling


class TestClassVsInstance(unittest.TestCase):
    def test_shared_class_attribute(self):
        module = ex01_class_vs_instance
        module.SharedTeam.members = []  # isolate repeated runs
        self.assertEqual(module.PREDICT_SHARED_COUNT, module.shared_scenario())

    def test_separate_instance_attribute(self):
        module = ex01_class_vs_instance
        self.assertEqual(module.PREDICT_SEPARATE_COUNT, module.separate_scenario())


class TestEqAndHash(unittest.TestCase):
    def test_default_equality_is_identity(self):
        module = ex02_eq_and_hash
        self.assertEqual(module.PREDICT_PLAIN_EQUAL,
                         module.PlainPoint(1, 2) == module.PlainPoint(1, 2))

    def test_value_equality(self):
        module = ex02_eq_and_hash
        self.assertEqual(module.PREDICT_VALUE_EQUAL,
                         module.ValuePoint(1, 2) == module.ValuePoint(1, 2))

    def test_eq_without_hash_kills_dict_keys(self):
        module = ex02_eq_and_hash
        self.assertEqual(module.PREDICT_KEY_FAILURE, module.key_failure_name())


class TestNameMangling(unittest.TestCase):
    def test_direct_access_fails(self):
        module = ex03_name_mangling
        self.assertEqual(module.PREDICT_DIRECT_FAILURE, module.direct_failure_name())

    def test_mangled_access_succeeds(self):
        module = ex03_name_mangling
        self.assertEqual(module.PREDICT_MANGLED_VALUE, module.mangled_read())


if __name__ == "__main__":
    unittest.main()

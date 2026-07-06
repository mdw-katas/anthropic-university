"""Self-checks for the Lesson 7 explorations: uni grade 101/explore-07"""
import unittest

import tally
import ex01_import_once
import ex02_main_name
import ex03_traceback


class TestImportOnce(unittest.TestCase):
    def test_run_count(self):
        self.assertEqual(ex01_import_once.PREDICT_RUN_COUNT, len(tally.RUNS))


class TestMainName(unittest.TestCase):
    def test_name_when_imported(self):
        self.assertEqual(ex02_main_name.PREDICT_NAME_WHEN_IMPORTED,
                         ex02_main_name.NAME)

    def test_name_when_run_directly(self):
        self.assertEqual(ex02_main_name.PREDICT_NAME_WHEN_RUN, "__main__")


class TestTraceback(unittest.TestCase):
    def test_exception_type(self):
        exception_type, _ = ex03_traceback.observe_crash()
        self.assertEqual(ex03_traceback.PREDICT_EXCEPTION_TYPE, exception_type)

    def test_raising_function(self):
        _, function = ex03_traceback.observe_crash()
        self.assertEqual(ex03_traceback.PREDICT_RAISING_FUNCTION, function)


if __name__ == "__main__":
    unittest.main()

"""Self-checks for the Lesson 7 explorations: uni grade 102/explore-07"""
import unittest
from unittest.mock import Mock

import ex01_inject_the_clock
import ex02_spy
import ex03_vacuous_mock


class TestInjectTheClock(unittest.TestCase):
    def test_idle_work_with_ticking_clock(self):
        module = ex01_inject_the_clock
        self.assertEqual(module.PREDICT_TICKING_ELAPSED,
                         module.elapsed_seconds(module.idle,
                                                module.make_ticking_clock(5)))

    def test_extra_reading_skews_the_measurement(self):
        module = ex01_inject_the_clock
        self.assertEqual(module.PREDICT_BUSY_ELAPSED,
                         module.elapsed_seconds(module.reads_clock_once,
                                                module.make_ticking_clock(3)))


class TestSpy(unittest.TestCase):
    def test_call_count(self):
        self.assertEqual(ex02_spy.PREDICT_CALL_COUNT,
                         len(ex02_spy.scenario().calls))

    def test_first_recorded_call(self):
        self.assertEqual(ex02_spy.PREDICT_FIRST_CALL,
                         ex02_spy.scenario().calls[0])


class TestVacuousMock(unittest.TestCase):
    def test_deploy_with_bare_mock(self):
        self.assertEqual(ex03_vacuous_mock.PREDICT_DEPLOY_RESULT,
                         ex03_vacuous_mock.deploy(Mock()))

    def test_mock_truthiness(self):
        self.assertEqual(ex03_vacuous_mock.PREDICT_MOCK_TRUTHY,
                         bool(Mock().anything.at.all()))

    def test_typo_goes_unpunished(self):
        self.assertEqual(ex03_vacuous_mock.PREDICT_TYPO_FAILURE,
                         ex03_vacuous_mock.typo_failure_name())


if __name__ == "__main__":
    unittest.main()

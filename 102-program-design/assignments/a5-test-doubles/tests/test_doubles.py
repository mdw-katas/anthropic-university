"""The executable specification for assignment a5."""
import pathlib
import sys
import time
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "starter"))

from doubles import FakeClock, Spy, StubSequence, retry


class TestFakeClock(unittest.TestCase):
    def test_starts_where_told(self):
        self.assertEqual(FakeClock().time(), 0.0)
        self.assertEqual(FakeClock(start=100.0).time(), 100.0)

    def test_sleep_advances_time(self):
        clock = FakeClock(start=10.0)
        clock.sleep(5.0)
        clock.sleep(2.5)
        self.assertEqual(clock.time(), 17.5)

    def test_sleep_records_each_wait(self):
        clock = FakeClock()
        clock.sleep(1.0)
        clock.sleep(4.0)
        self.assertEqual(clock.sleeps, [1.0, 4.0])

    def test_negative_sleep_is_rejected(self):
        clock = FakeClock()
        with self.assertRaises(ValueError):
            clock.sleep(-1.0)
        self.assertEqual(clock.time(), 0.0, "a rejected sleep must not advance time")


class TestSpy(unittest.TestCase):
    def test_records_args_and_kwargs(self):
        spy = Spy()
        spy("subject", cc="boss")
        spy(42)
        self.assertEqual(spy.calls, [(("subject",), {"cc": "boss"}), ((42,), {})])
        self.assertEqual(spy.call_count, 2)

    def test_returns_the_canned_result(self):
        spy = Spy(result="accepted")
        self.assertEqual(spy("anything"), "accepted")
        self.assertEqual(spy(), "accepted")

    def test_fresh_spies_do_not_share_recordings(self):
        first, second = Spy(), Spy()
        first("only mine")
        self.assertEqual(second.call_count, 0)


class TestStubSequence(unittest.TestCase):
    def test_returns_scripted_values_in_order(self):
        stub = StubSequence(["alpha", "beta"])
        self.assertEqual(stub(), "alpha")
        self.assertEqual(stub(), "beta")

    def test_exception_instances_are_raised(self):
        stub = StubSequence([ConnectionError("down"), "recovered"])
        with self.assertRaises(ConnectionError):
            stub()
        self.assertEqual(stub(), "recovered")

    def test_exhausted_stub_fails_loudly(self):
        stub = StubSequence(["only one"])
        stub()
        with self.assertRaises(AssertionError):
            stub()


def forbid_real_sleep(test):
    """Booby-trap time.sleep for the duration of one test."""
    def tripwire(_seconds):
        raise AssertionError("retry called time.sleep — use the injected clock")
    original = time.sleep
    time.sleep = tripwire
    test.addCleanup(setattr, time, "sleep", original)


class TestRetry(unittest.TestCase):
    def setUp(self):
        forbid_real_sleep(self)

    def test_immediate_success_never_sleeps(self):
        clock = FakeClock()
        result = retry(StubSequence(["done"]), attempts=3, delay=1.0, clock=clock)
        self.assertEqual(result, "done")
        self.assertEqual(clock.sleeps, [])

    def test_backoff_doubles_between_failures(self):
        clock = FakeClock()
        action = StubSequence([IOError("a"), IOError("b"), "third time lucky"])
        result = retry(action, attempts=5, delay=1.0, clock=clock)
        self.assertEqual(result, "third time lucky")
        self.assertEqual(clock.sleeps, [1.0, 2.0])

    def test_final_failure_reraises_without_a_trailing_sleep(self):
        clock = FakeClock()
        action = StubSequence([IOError("a"), IOError("b"), IOError("c")])
        with self.assertRaises(IOError):
            retry(action, attempts=3, delay=2.0, clock=clock)
        self.assertEqual(clock.sleeps, [2.0, 4.0],
                         "no sleep after the last attempt — nothing left to wait for")

    def test_gives_up_after_exactly_attempts_calls(self):
        clock = FakeClock()
        failing = StubSequence([ValueError("x"), ValueError("y"), ValueError("z"),
                                "never reached"])
        with self.assertRaises(ValueError):
            retry(failing, attempts=3, delay=1.0, clock=clock)
        self.assertEqual(failing(), "never reached",
                         "retry made a fourth call it was not entitled to")

    def test_rejects_senseless_attempts(self):
        exploding = StubSequence([AssertionError("action must not be called")])
        with self.assertRaises(ValueError):
            retry(exploding, attempts=0, delay=1.0, clock=FakeClock())

    def test_the_doubles_compose_into_a_deterministic_story(self):
        clock = FakeClock(start=50.0)
        action = StubSequence([TimeoutError("t1"), TimeoutError("t2"), "ok"])
        result = retry(action, attempts=4, delay=0.5, clock=clock)
        self.assertEqual(result, "ok")
        self.assertEqual(clock.time(), 51.5, "50.0 + 0.5 + 1.0 of fake waiting")


if __name__ == "__main__":
    unittest.main()

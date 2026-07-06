"""Exploration: naive fib's call tree — count every call.

fib(0) and fib(1) each cost one call. calls(n) = 1 + calls(n-1) + calls(n-2).
Work out fib(5)'s totals on paper (the lesson's widget agrees with you),
run this file, then: uni grade 101/explore-05
"""

PREDICT_VALUE_FOR_5 = None
PREDICT_CALLS_FOR_5 = None


def fib_counting(n):
    calls = 0

    def fib(k):
        nonlocal calls
        calls += 1
        if k <= 1:
            return k
        return fib(k - 1) + fib(k - 2)

    value = fib(n)
    return value, calls


if __name__ == "__main__":
    value, calls = fib_counting(5)
    print(f"fib(5) = {value}, computed with {calls} calls")

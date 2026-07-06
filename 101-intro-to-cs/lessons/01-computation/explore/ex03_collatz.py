"""Exploration 3: the Collatz process — simple rules, wild behavior.

From any positive integer n: if n is even, halve it; if odd, replace it
with 3n + 1. Repeat until you reach 1. Nobody has proved this always
terminates — yet every number ever tried gets there.

Trace n = 6 by hand and count the steps. Then, for the champion
question, think (or trace) before you run: which starting number in
1..10 takes the MOST steps to reach 1?

Fill in predictions, run this file to check, then:
uni grade 101/explore-01
"""

PREDICT_STEPS_FOR_6 = None
PREDICT_CHAMPION_UNDER_10 = None  # the n in 1..10 with the most steps


def collatz_steps(n):
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        steps += 1
    return steps


def champion(limit):
    best, best_steps = 1, 0
    for n in range(1, limit + 1):
        steps = collatz_steps(n)
        if steps > best_steps:
            best, best_steps = n, steps
    return best


if __name__ == "__main__":
    for n in range(1, 11):
        print(f"collatz_steps({n}) = {collatz_steps(n)}")
    print(f"champion in 1..10: {champion(10)}")

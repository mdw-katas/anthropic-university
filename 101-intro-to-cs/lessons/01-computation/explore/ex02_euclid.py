"""Exploration 2: Euclid's algorithm, the lesson's worked classic.

Using only pencil and paper, run Euclid's algorithm on (1071, 462):
repeatedly replace (a, b) with (b, a % b) until b is 0.

Fill in your predictions, run this file to check, then:
uni grade 101/explore-01
"""

PREDICT_GCD = 21    # gcd(1071, 462)
PREDICT_STEPS = 3   # how many replacement steps until b == 0


def gcd_with_steps(a, b):
    steps = 0
    while b != 0:
        a, b = b, a % b
        steps += 1
    return a, steps


if __name__ == "__main__":
    value, steps = gcd_with_steps(1071, 462)
    print(f"gcd(1071, 462) = {value} in {steps} steps")

"""
a: 1071
b: 462
steps: 0

a: 462
b: 147
steps: 1

a: 147
b: 21
steps: 2

a: 21
b: 0
steps: 3
"""
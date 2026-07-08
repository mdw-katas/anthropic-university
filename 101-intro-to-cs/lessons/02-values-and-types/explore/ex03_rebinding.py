"""Exploration: assignment rebinds names; it never changes values.

Predict, run, then: uni grade 101/explore-02
"""

PREDICT_Y = "hello"  # see rebind() below
PREDICT_B = 5


def rebind():
    x = "hello"
    y = x
    x = x + "!"
    return x, y


def arithmetic():
    a = 5
    b = a
    a = a * 2
    return a, b


if __name__ == "__main__":
    x, y = rebind() # "hello!" "hello"
    print(f"x = {x!r}, y = {y!r}")
    a, b = arithmetic() # 10 5
    print(f"a = {a}, b = {b}")

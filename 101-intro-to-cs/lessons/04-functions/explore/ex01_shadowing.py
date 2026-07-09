"""Exploration: assignment inside a function creates a LOCAL name.

Predict, run, then: uni grade 101/explore-04
"""

PREDICT_SHADOW_RETURN = 5   # shadow()
PREDICT_MODULE_X_AFTER = 10  # x, after shadow() has been called

x = 10


def shadow():
    x = 5
    return x


if __name__ == "__main__":
    print(f"shadow() = {shadow()}")
    print(f"module-level x after calling shadow() = {x}")

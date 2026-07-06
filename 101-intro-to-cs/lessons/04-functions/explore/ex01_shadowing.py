"""Exploration: assignment inside a function creates a LOCAL name.

Predict, run, then: uni grade 101/explore-04
"""

PREDICT_SHADOW_RETURN = None   # shadow()
PREDICT_MODULE_X_AFTER = None  # x, after shadow() has been called

x = 10


def shadow():
    x = 5
    return x


if __name__ == "__main__":
    print(f"shadow() = {shadow()}")
    print(f"module-level x after calling shadow() = {x}")

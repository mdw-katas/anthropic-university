"""Exploration: integer division, modulo, and float equality.

Python FLOORS division (C truncates), and % takes the sign of the
divisor. Predict on paper, run this file, then:
uni grade 101/explore-02
"""

PREDICT_FLOOR_DIV = None    # -7 // 2
PREDICT_MOD = None          # -7 % 2
PREDICT_FLOAT_EQUAL = None  # 0.1 + 0.2 == 0.3  (True or False?)


if __name__ == "__main__":
    print(f"-7 // 2         = {-7 // 2}")
    print(f"-7 % 2          = {-7 % 2}")
    print(f"0.1 + 0.2 == 0.3  is {0.1 + 0.2 == 0.3}")
    print(f"0.1 + 0.2       = {0.1 + 0.2!r}")

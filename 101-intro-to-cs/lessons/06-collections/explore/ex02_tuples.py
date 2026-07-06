"""Exploration: tuple immutability is one level deep.

t = ([1, 2], "x") — the tuple's arrows are frozen; what they point at
may not be. Predict both, run, then: uni grade 101/explore-06
"""

PREDICT_LIST_INSIDE = None      # t[0] after t[0].append(3)
PREDICT_REPLACE_RAISES = None   # does t[1] = "y" raise TypeError? True/False


def mutate_inside():
    t = ([1, 2], "x")
    t[0].append(3)
    return t[0]


def try_replace():
    t = ([1, 2], "x")
    try:
        t[1] = "y"
        return False
    except TypeError:
        return True


if __name__ == "__main__":
    print(f"t[0] after t[0].append(3): {mutate_inside()}")
    print(f"t[1] = 'y' raises TypeError: {try_replace()}")

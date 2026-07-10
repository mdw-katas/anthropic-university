"""Exploration: the Method Resolution Order in a diamond.

Every greet() contributes its letter, then defers to super() — "next in
the MRO," which is not always the parent. Predict the string D().greet()
builds, and which class comes second in D's MRO.

Fill the PREDICT_* constants, run this file, then:
uni grade 102/explore-04
"""

PREDICT_D_GREET = None      # D().greet(), e.g. "ABC"
PREDICT_SECOND_IN_MRO = None  # class NAME right after D in D's MRO, e.g. "A"


class A:
    def greet(self):
        return "A"


class B(A):
    def greet(self):
        return "B" + super().greet()


class C(A):
    def greet(self):
        return "C" + super().greet()


class D(B, C):
    pass


def mro_names():
    return [cls.__name__ for cls in D.__mro__]


if __name__ == "__main__":
    print(f"D().greet() = {D().greet()!r}")
    print(f"D MRO: {' -> '.join(mro_names())}")
    # B's super() is C here, not A. super() means "next in line."

"""Exploration: Square IS-A Rectangle, says geometry. Says the contract?

stretch() was written against Rectangle's contract: "set_width and
set_height act independently." Predict its result for each class.

Fill the PREDICT_* constants, run this file, then:
uni grade 102/explore-04
"""

PREDICT_RECTANGLE_AREA = None  # stretch(Rectangle(1, 1))
PREDICT_SQUARE_AREA = None     # stretch(Square(1))


class Rectangle:
    def __init__(self, width, height):
        self._width, self._height = width, height

    def set_width(self, width):
        self._width = width

    def set_height(self, height):
        self._height = height

    def area(self):
        return self._width * self._height


class Square(Rectangle):
    """Keeps its sides equal — and thereby breaks its parent's contract."""

    def __init__(self, side):
        super().__init__(side, side)

    def set_width(self, width):
        self._width = self._height = width

    def set_height(self, height):
        self._width = self._height = height


def stretch(rectangle):
    """Written against Rectangle's contract; never heard of Square."""
    rectangle.set_width(4)
    rectangle.set_height(5)
    return rectangle.area()


if __name__ == "__main__":
    print(f"stretch(Rectangle(1, 1)) = {stretch(Rectangle(1, 1))}")
    print(f"stretch(Square(1))       = {stretch(Square(1))}")
    # Substitutability is about contracts, not taxonomy.

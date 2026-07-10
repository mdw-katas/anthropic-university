"""Self-checks for the Lesson 4 explorations: uni grade 102/explore-04"""
import unittest

import ex01_mro
import ex02_fragile_base
import ex03_square_rectangle


class TestMRO(unittest.TestCase):
    def test_diamond_greeting(self):
        self.assertEqual(ex01_mro.PREDICT_D_GREET, ex01_mro.D().greet())

    def test_second_in_mro(self):
        self.assertEqual(ex01_mro.PREDICT_SECOND_IN_MRO, ex01_mro.mro_names()[1])


class TestFragileBase(unittest.TestCase):
    def test_subclass_misses_writes(self):
        self.assertEqual(ex02_fragile_base.PREDICT_SUBCLASS_LOGGED,
                         ex02_fragile_base.subclass_scenario())

    def test_composition_catches_all_writes(self):
        self.assertEqual(ex02_fragile_base.PREDICT_COMPOSED_LOGGED,
                         ex02_fragile_base.composed_scenario())


class TestSquareRectangle(unittest.TestCase):
    def test_rectangle_obeys_the_contract(self):
        module = ex03_square_rectangle
        self.assertEqual(module.PREDICT_RECTANGLE_AREA,
                         module.stretch(module.Rectangle(1, 1)))

    def test_square_breaks_the_contract(self):
        module = ex03_square_rectangle
        self.assertEqual(module.PREDICT_SQUARE_AREA,
                         module.stretch(module.Square(1)))


if __name__ == "__main__":
    unittest.main()

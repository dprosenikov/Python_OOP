import unittest

from project.factory.paint_factory import PaintFactory


class TestPaintFactory(unittest.TestCase):
    def test_name_is_initialized(self):
        fact = PaintFactory('F1', 15)
        self.assertTrue(fact, 'S1')

    def test_capacity_is_initialized(self):
        fact = PaintFactory('F1', 15)
        self.assertEqual(fact.capacity, 15)


    def test_ingrediaent_is_empty_upon_initialized(self):
        fact = PaintFactory('F1', 15)
        self.assertEqual(fact.ingredients, {})

    def test_ingredient_not_in_list(self):
        fact = PaintFactory('F1', 15)
        with self.assertRaises(TypeError):
            fact.add_ingredient('gosho', 10)

    def test_capacity_lt_quant(self):
        fact = PaintFactory('F1', 15)
        with self.assertRaises(ValueError):
            fact.add_ingredient('white', 16)

    def test_ingredient_is_added(self):
        fact = PaintFactory('F1', 15)
        fact.add_ingredient('yellow', 5)
        self.assertEqual(fact.ingredients, {'yellow': 5})

    def test_remove_nonexistent_ingredient(self):
        fact = PaintFactory('F1', 15)
        with self.assertRaises(KeyError):
            fact.remove_ingredient('yellow', 10)

    def test_remove_greater_quantity_than_what_we_have(self):
        fact = PaintFactory('F1', 15)
        fact.add_ingredient('yellow', 5)
        with self.assertRaises(ValueError):
            fact.remove_ingredient('yellow', 6)

    def test_ingredient_is_removed(self):
        fact = PaintFactory('F1', 15)
        fact.add_ingredient('yellow', 5)
        fact.remove_ingredient('yellow', 2)
        self.assertEqual(fact.ingredients, {'yellow': 3})

    def test_property(self):
        fact = PaintFactory('F1', 15)
        fact.add_ingredient('yellow', 5)
        self.assertEqual(fact.products, {'yellow': 5})

if __name__ == '__main__':
    unittest.main()
import unittest


from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    
    def test_rectangle_attributes_value(self):
        rectangle1 = Rectangle(1, 2)
        rectangle2 = Rectangle(1, 2, 3)
        rectangle3 = Rectangle(1, 2, 3, 4)
        # rectangle4 = Rectangle("1", 2)
        self.assertEqual(rectangle1.id, 1)
        self.assertRaises(TypeError, R)
        
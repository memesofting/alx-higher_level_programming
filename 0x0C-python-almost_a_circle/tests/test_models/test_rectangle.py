import unittest


from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    
    def test_attributes_assignment(self):
        rectangle1 = Rectangle(1, 2)
        rectangle2 = Rectangle(1, 2, 3)
        rectangle3 = Rectangle(1, 2, 3, 4)
        rectangle4 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(rectangle1.width, 1)
        self.assertEqual(rectangle1.height, 2)
        self.assertEqual(rectangle2.width, 1)
        self.assertEqual(rectangle2.height, 2)
        self.assertEqual(rectangle3.x, 3)
        self.assertEqual(rectangle3.y, 4)
        self.assertEqual(rectangle4.id, 5)
        
    def test_string_attributes_value(self):
        with self.assertRaises(TypeError):
            rectangle5  = Rectangle("1", 2)
        with self.assertRaises(TypeError):
            rectangle6  = Rectangle(1, "2")
        with self.assertRaises(TypeError):
            rectangle7  = Rectangle(1, 2, "3")
        with self.assertRaises(TypeError):
            rectangle8  = Rectangle(1, 2, 3, "4")
    def test_negative_attributes_value(self):
        with self.assertRaises(ValueError):
            rectangle9 = Rectangle(-1, 2)
        with self.assertRaises(ValueError):
            rectangle10 = Rectangle(1, -2)
        with self.assertRaises(ValueError):
            rectangle9 = Rectangle(0, 2)
        with self.assertRaises(ValueError):
            rectangle11 = Rectangle(1, 0)
        with self.assertRaises(ValueError):
            rectangle12 = Rectangle(1, 2, -3)
        with self.assertRaises(ValueError):
            rectangle12 = Rectangle(1, 2, 3, -4)
        
            
if __name__ == "__main__":
    unittest.main()
        
import unittest
from unittest.mock import patch
import io

from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test cases for Rectangle class"""

    def test_attributes_assignment(self):
        """Tests attributes assignment"""
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
        """Tests for string attributes input"""
        with self.assertRaises(TypeError):
            rectangle5 = Rectangle("1", 2)
        with self.assertRaises(TypeError):
            rectangle6 = Rectangle(1, "2")
        with self.assertRaises(TypeError):
            rectangle7 = Rectangle(1, 2, "3")
        with self.assertRaises(TypeError):
            rectangle8 = Rectangle(1, 2, 3, "4")

    def test_negative_attributes_value(self):
        """Tests for negative attributes value"""
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

    def test_area(self):
        """Checks for area method in Rectangle class"""
        self.assertTrue(hasattr(Rectangle, "area"), "method does not exist")

    def test_display(self):
        """Checks for display method in Rectangle class"""
        self.assertTrue(hasattr(Rectangle, "display"), "method does not exist")

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_output(self, mock_stdout):
        """Tests display method output"""
        r1 = Rectangle(2, 3, 2, 2)
        r1.display()
        self.assertEqual(mock_stdout.getvalue(), "\n\n  ##\n  ##\n  ##\n")

    def test_str(self):
        """Test __str__ override"""
        rectangle = Rectangle(3, 4, 5, 6, 7)
        self.assertEqual(str(rectangle), "[Rectangle] (7) 5/6 - 3/4")

    def test_update(self):
        """Checks for update method in Rectangle class"""
        self.assertTrue(hasattr(Rectangle, "update"), "method does not exist")

    def test_update_args(self):
        """Tests update method with arguments output"""
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 10/10")
        r1.update(89, 1)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 1/10")
        r1.update(89, 1, 2)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 1/2")
        r1.update(89, 1, 2, 3)
        self.assertEqual(str(r1), "[Rectangle] (89) 3/10 - 1/2")
        r1.update(89, 1, 2, 3, 4)
        self.assertEqual(str(r1), "[Rectangle] (89) 3/4 - 1/2")
        r1.update(id=90)
        # self.assertEqual(str(r1), "[Rectangle] (90) 3/4 - 1/2")
        self.assertEqual(r1.id, 90)


if __name__ == "__main__":
    unittest.main()

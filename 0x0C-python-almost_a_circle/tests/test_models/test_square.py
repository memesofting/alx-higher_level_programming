import unittest

from models.square import Square


class TestSquare(unittest.TestCase):
    """Square class test cases"""

    def test_square_area(self):
        """test for square area"""
        s1 = Square(5)
        s2 = Square(2, 2)
        s3 = Square(3, 1, 3)
        self.assertEqual(s1.area(), 25)
        self.assertEqual(s2.area(), 4)
        self.assertEqual(s3.area(), 9)

    def test_size(self):
        """Test square size"""
        with self.assertRaises(TypeError):
            s = Square("9")

    def test_update(self):
        """Test swuare update function"""
        s = Square(5)
        s.update(10, 2, 3, 4)
        self.assertEqual(str(s), "[Square] (10) 4/0 - 2")


if __name__ == "__main__":
    unittest.main()

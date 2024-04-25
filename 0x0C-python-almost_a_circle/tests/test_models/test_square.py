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
    
    def test_str(self):
        """Test __str__override"""
        s1 = Square(5)
        self.assertEqual(str(s1), "[Square] (5) 0/0 - 5")
        
    def test_size(self):
        self.assertRaises(Square("9"), "[TypeError] width must be an integer")
        
if __name__ == "__main__":
    unittest.main()

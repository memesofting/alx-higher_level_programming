import unittest


from models.base import Base


class TestBase(unittest.TestCase):

    def test_id_increment(self):
        base1 = Base()
        base2 = Base()
        base3 = Base()
        self.assertEqual(base3.id, 3)

    def test_id_argument(self):
        base3 = Base(34)
        base5 = Base(36)
        self.assertEqual(base3.id, 34)
        self.assertEqual(base5.id, 36)


if __name__ == "__main__":
    unittest.main()

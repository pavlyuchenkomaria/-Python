import unittest


def my_sum(a, b):
    return a + b

class SumTests(unittest.TestCase):
    def test_add(self):
        self.assertEqual(my_sum(1, 2), 3)

if __name__ == '__main__':
    unittest.main()
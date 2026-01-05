import unittest
from app import hello, calcule, say_hello


class TestApp(unittest.TestCase):

    def test_hello(self):
        self.assertEqual(hello("Ababacar"), "Bonjour Ababacar 👋")

    def test_calcule(self):
        self.assertEqual(calcule(2, 3), 5)
        self.assertEqual(calcule(-1, 1), 0)
        self.assertEqual(calcule(0, 0), 0)


if __name__ == "__main__":
    unittest.main()

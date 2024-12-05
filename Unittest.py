import unittest
from app import addition, subtraction, multiplication, division, modulus, power, square_root, sine, cosine
from app import Memory

class TestCalcOperations(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(addition(2, 3), 5)
        self.assertEqual(addition(-2, 3), 1)
        self.assertEqual(addition(0, 0), 0)

    def test_subtraction(self):
        self.assertEqual(subtraction(3, 2), 1)
        self.assertEqual(subtraction(2, 3), -1)
        self.assertEqual(subtraction(0, 0), 0)

    def test_multiplication(self):
        self.assertEqual(multiplication(2, 3), 6)
        self.assertEqual(multiplication(-2, 3), -6)
        self.assertEqual(multiplication(0, 3), 0)

    def test_division(self):
        self.assertEqual(division(6, 3), 2)
        self.assertEqual(division(5, 2), 2.5)
        with self.assertRaises(ValueError):
            division(6, 0)

    def test_modulus(self):
        self.assertEqual(modulus(5, 3), 2)
        self.assertEqual(modulus(5, 5), 0)

    def test_power(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(5, 0), 1)

    def test_sine(self):
        self.assertEqual(sine(0), 0)
        self.assertAlmostEqual(sine(90), 1, places=5)

    def test_cosine(self):
        self.assertEqual(cosine(0), 1)
        self.assertAlmostEqual(cosine(90), 0, places=5)

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            addition("a", 3)  # Неверный символ
        with self.assertRaises(ValueError):
            subtraction(3, "b")  # Неверный символ
        with self.assertRaises(ValueError):
            multiplication("!", 3)  # Неверный символ
        with self.assertRaises(ValueError):
            division(3, "@"); # Неверный символ

class TestMemory(unittest.TestCase):

    def setUp(self):
        self.memory = Memory()

    def test_memory_add(self):
        self.memory.m_add(10)
        self.assertEqual(self.memory.m_recall(), 10)

    def test_memory_subtract(self):
        self.memory.m_add(10)
        self.memory.m_subtract(5)
        self.assertEqual(self.memory.m_recall(), 5)

    def test_memory_clear(self):
        self.memory.m_add(10)
        self.memory.m_clear()
        self.assertEqual(self.memory.m_recall(), 0)

if __name__ == "__main__":
    unittest.main()

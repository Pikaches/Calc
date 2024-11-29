import unittest
from calc_operations import addition, subtraction, multiplication, division, modulus, power, square_root, sine, cosine, Memory

class TestCalcOperations(unittest.TestCase):

    # Тесты для базовых операций с валидацией
    def test_addition(self):
        self.assertEqual(addition(2, 3), 5)
        self.assertEqual(addition(-1, 1), 0)
        with self.assertRaises(ValueError):
            addition("invalid", 3)  # Проверка некорректного ввода

    def test_subtraction(self):
        self.assertEqual(subtraction(5, 3), 2)
        self.assertEqual(subtraction(2, 5), -3)
        with self.assertRaises(ValueError):
            subtraction("invalid", 3)  # Проверка некорректного ввода

    def test_multiplication(self):
        self.assertEqual(multiplication(3, 4), 12)
        self.assertEqual(multiplication(-2, 3), -6)
        with self.assertRaises(ValueError):
            multiplication("invalid", 3)  # Проверка некорректного ввода

    def test_division(self):
        self.assertEqual(division(10, 2), 5)
        with self.assertRaises(ValueError):
            division(10, 0)  # Проверка деления на ноль
        with self.assertRaises(ValueError):
            division("invalid", 5)  # Проверка некорректного ввода

    def test_modulus(self):
        self.assertEqual(modulus(10, 3), 1)
        self.assertEqual(modulus(10, 5), 0)
        with self.assertRaises(ValueError):
            modulus("invalid", 3)  # Проверка некорректного ввода

    def test_power(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(5, 0), 1)
        with self.assertRaises(ValueError):
            power("invalid", 3)  # Проверка некорректного ввода

    def test_square_root(self):
        self.assertEqual(square_root(9), 3)
        with self.assertRaises(ValueError):
            square_root(-9)  # Проверка ошибки при отрицательном числе

    # Тесты для тригонометрических функций
    def test_sine(self):
        self.assertEqual(sine(0), 0)
        self.assertEqual(sine(90), 1)
        with self.assertRaises(ValueError):
            sine("invalid")  # Проверка некорректного ввода

    def test_cosine(self):
        self.assertEqual(cosine(0), 1)
        self.assertEqual(cosine(90), 0)
        with self.assertRaises(ValueError):
            cosine("invalid")  # Проверка некорректного ввода

    # Тестирование класса Memory с валидацией
    def test_memory_operations(self):
        memory = Memory()
        memory.m_add(5)
        self.assertEqual(memory.memory, 5)
        memory.m_subtract(2)
        self.assertEqual(memory.memory, 3)
        memory.m_multiply(2)
        self.assertEqual(memory.memory, 6)
        memory.m_divide(3)
        self.assertEqual(memory.memory, 2)
        memory.m_clear()
        self.assertEqual(memory.memory, 0)

        # Проверка с некорректным вводом
        with self.assertRaises(ValueError):
            memory.m_add("invalid")  # Проверка на некорректное значение

    # Тестирование ввода (валидность)
    def test_invalid_decimal_input(self):
        with self.assertRaises(ValueError):
            Memory().m_add("invalid")  # Проверка с некорректным значением
        with self.assertRaises(ValueError):
            division("invalid", 5)  # Проверка с некорректным значением

if __name__ == '__main__':
    unittest.main()

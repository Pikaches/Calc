import math
import decimal  # Добавьте этот импорт
from decimal import Decimal

def addition(a, b):
    a = validate_decimal(a)  # Валидация входных данных
    b = validate_decimal(b)  # Валидация входных данных
    return a + b

def subtraction(a, b):
    a = validate_decimal(a)
    b = validate_decimal(b)
    return a - b

def multiplication(a, b):
    a = validate_decimal(a)
    b = validate_decimal(b)
    return a * b

def division(a, b):
    a = validate_decimal(a)
    b = validate_decimal(b)
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def modulus(a, b):
    a = validate_decimal(a)
    b = validate_decimal(b)
    return a % b

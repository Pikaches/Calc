import math
import decimal  # Добавьте этот импорт
from decimal import Decimal

def addition(a, b):
    a = validate_decimal(a)  # Валидация входных данных
    b = validate_decimal(b)  # Валидация входных данных
    return a + b

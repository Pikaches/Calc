import tkinter as tk
from tkinter import ttk  # Используем ttk для современного стиля кнопок
from calc_oper import (
    addition, subtraction, multiplication, division, modulus, power,
    square_root, sine, cosine, floor_value, ceil_value,
)
from calc_oper import Memory

memory = Memory()  # Инициализация объекта памяти
entry_text = None  # Переменная для хранения текста ввода

def on_button_click(value):
    entry_text.set(entry_text.get() + value)
    
def on_clear():
    entry_text.set("")  # Сбрасываем текст ввода
    
def on_backspace():
    current_text = entry_text.get()
    entry_text.set(current_text[:-1])

def on_equal():
    try:
        expression = entry_text.get().replace("^", "**")  # Заменяем ^ на **
        result = eval(expression)  # Вычисляем результат выражения
        entry_text.set(result)  # Отображаем результат
    except ZeroDivisionError:
        entry_text.set("Error: Division by zero")  # Обработка деления на ноль
    except SyntaxError:
        entry_text.set("Error: Invalid syntax")  # Обработка синтаксической ошибки
    except Exception as e:
        entry_text.set(f"Error: {e}")  # Обработка других исключений

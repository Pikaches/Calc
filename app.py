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

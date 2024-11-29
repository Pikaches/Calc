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

def on_memory_add():
    try:
        value = float(entry_text.get())  # Получаем значение из ввода
        memory.m_add(value)  # Добавляем значение в память
        entry_text.set("")  # Очищаем строку ввода
    except ValueError:
        entry_text.set("Error: Invalid input")  # Обработка некорректного ввода

def on_memory_recall():
    entry_text.set(str(memory.m_recall()))  # Устанавливаем значение памяти в ввод

def on_memory_clear():
    memory.m_clear()  # Очищаем память
    entry_text.set("")  # Очищаем строку ввода

def start_calculator():
    global entry_text
    window = tk.Tk()  # Создаем главное окно приложения
    window.title("Calculator")  # Устанавливаем заголовок окна
    window.geometry("400x600")  # Устанавливаем размеры окна
    window.configure(bg="#282c34")  # Устанавливаем темный фон

    entry_text = tk.StringVar()  # Инициализируем переменную для текста ввода

    entry = tk.Entry(
        window, textvariable=entry_text, font=('Arial', 24),
        bd=10, relief="flat", justify="right", bg="#1e2227", fg="#ffffff"
    )
    entry.grid(row=0, column=0, columnspan=4, pady=(10, 20), padx=10, sticky="nsew")
    
    style = ttk.Style()  # Настройка стиля для кнопок
    style.configure("TButton", font=('Arial', 14), padding=10)
    style.map("TButton",
              foreground=[('pressed', '#282c34'), ('active', '#ffffff')],
              background=[('pressed', '#61afef'), ('active', '#61afef')])


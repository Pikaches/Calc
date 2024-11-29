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

    buttons = [  # Определение кнопок калькулятора и их расположение
        ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
        ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
        ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
        ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
        ('MC', 5, 0), ('MR', 5, 1), ('M+', 5, 2), ('M-', 5, 3),
        ('Clear', 6, 0), ('C', 6, 1), ('←', 6, 2), ('%', 6, 3)
    ]

    for (text, row, col) in buttons: 
        command = (
            on_equal if text == "=" else
            on_clear if text == "C" or text == "Clear" else
            on_memory_clear if text == "MC" else
            on_memory_recall if text == "MR" else
            on_memory_add if text == "M+" else
            on_memory_subtract if text == "M-" else
            on_backspace if text == "←" else
            lambda t=text: on_button_click(t)  
        )
        ttk.Button(window, text=text, command=command).grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

    for i in range(7):  
        window.grid_rowconfigure(i, weight=1)  
    for i in range(4):  
        window.grid_columnconfigure(i, weight=1)

    window.mainloop()   # Запуск главного цикла приложения

if __name__ == "__main__":
    start_calculator()   # Запуск калькулятора при исполнении скрипта

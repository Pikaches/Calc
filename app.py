import tkinter as tk
from tkinter import ttk
from calc_oper import (
    addition, subtraction, multiplication, division, modulus, power,
    square_root, sine, cosine, floor_value, ceil_value,
)
from calc_oper import Memory

memory = Memory()
entry_text = None
binary_label = None
octal_label = None


def on_button_click(value):
    entry_text.insert(tk.END, value)  # Добавление значения в поле ввода


def on_clear():
    entry_text.delete("1.0", tk.END)  # Очищает поле
    if binary_label and octal_label:
        binary_label.config(text="")
        octal_label.config(text="")


def on_backspace():
    current_text = entry_text.get("1.0", tk.END).strip()
    entry_text.delete("1.0", tk.END)  # Удаляем всё
    entry_text.insert(tk.END, current_text[:-1])  # Удаляем последний символ


def on_equal():
    try:
        expression = entry_text.get("1.0", tk.END).strip()
        allowed_chars = "0123456789+-*/().%"
        if not all(char in allowed_chars for char in expression):
            raise ValueError("Недопустимые символы в выражении")
        result = eval(expression)
        entry_text.delete("1.0", tk.END)
        entry_text.insert(tk.END, result)

        if binary_label and octal_label:
            binary_label.config(text=f"Бинарное: {bin(int(result))[2:]}")
            octal_label.config(text=f"Октальное: {oct(int(result))[2:]}")

    except ZeroDivisionError:
        entry_text.delete("1.0", tk.END)
        entry_text.insert(tk.END, "Ошибка: деление на ноль")
    except Exception as e:
        entry_text.delete("1.0", tk.END)
        entry_text.insert(tk.END, f"Ошибка: {e}")


def on_memory_add():
    try:
        value = float(entry_text.get("1.0", tk.END).strip())
        memory.m_add(value)
        entry_text.delete("1.0", tk.END)
    except ValueError:
        entry_text.delete("1.0", tk.END)
        entry_text.insert(tk.END, "Ошибка: неверный ввод")  # Ошибка ввода


def on_memory_subtract():
    try:
        value = float(entry_text.get("1.0", tk.END).strip())
        memory.m_subtract(value)
        entry_text.delete("1.0", tk.END)
    except ValueError:
        entry_text.delete("1.0", tk.END)
        entry_text.insert(tk.END, "Ошибка: неверный ввод")  # Ошибка ввода


def on_memory_recall():
    entry_text.delete("1.0", tk.END)
    entry_text.insert(tk.END, str(memory.m_recall()))  # Отображение значения из памяти


def on_memory_clear():
    memory.m_clear()  # Очистка памяти
    entry_text.delete("1.0", tk.END)


def on_system_conversion():
    try:
        expression = entry_text.get("1.0", tk.END).strip()
        result = eval(expression)

        # Переводим результат в двоичную и восьмиричную системы
        if binary_label and octal_label:
            binary_label.config(text=f"Бинарное: {bin(int(result))[2:]}")
            octal_label.config(text=f"Октальное: {oct(int(result))[2:]}")
    except Exception as e:
        entry_text.delete("1.0", tk.END)
        entry_text.insert(tk.END, f"Ошибка: {e}")  # Общая ошибка


def start_calculator():
    global entry_text, binary_label, octal_label
    window = tk.Tk()
    window.title("Калькулятор")
    window.geometry("752x600")
    window.configure(bg="#282c34")  # Устанавливаем темный фон

    frame = tk.Frame(window, bg="#282c34")
    frame.grid(row=0, column=0, columnspan=4, padx=10, pady=(10, 20), sticky="nsew")

    # Добавляем текстовое поле с полосой прокрутки
    entry_text = tk.Text(
        frame, font=('Arial', 24), bd=10, relief="flat",
        height=2, bg="#1e2227", fg="#ffffff", wrap="none"
    )
    entry_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar = tk.Scrollbar(frame, orient="horizontal", command=entry_text.xview)
    scrollbar.pack(side=tk.BOTTOM, fill=tk.X)
    entry_text.configure(xscrollcommand=scrollbar.set)

    style = ttk.Style()
    style.configure("TButton", font=('Arial', 14), padding=10)
    style.map("TButton",
              foreground=[('pressed', '#282c34'), ('active', '#ffffff')],
              background=[('pressed', '#61afef'), ('active', '#61afef')])

    buttons = [
        ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
        ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
        ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
        ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
        ('MC', 5, 0), ('MR', 5, 1), ('M+', 5, 2), ('M-', 5, 3),
        ('C', 6, 0), ('←', 6, 1), ('%', 6, 2), ('СС', 6, 3),
    ]

    for (text, row, col) in buttons:
        command = (
            on_equal if text == "=" else
            on_clear if text == "C" else
            on_memory_clear if text == "MC" else
            on_memory_recall if text == "MR" else
            on_memory_add if text == "M+" else
            on_memory_subtract if text == "M-" else
            on_backspace if text == "←" else
            on_system_conversion if text == "СС" else
            lambda t=text: on_button_click(t)
        )
        ttk.Button(window, text=text, command=command).grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

    # Метки для отображения перевода
    binary_label = tk.Label(window, text="", font=("Arial", 14), fg="#ffffff", bg="#282c34")
    binary_label.grid(row=7, column=0, columnspan=4, padx=5, pady=5)

    octal_label = tk.Label(window, text="", font=("Arial", 14), fg="#ffffff", bg="#282c34")
    octal_label.grid(row=8, column=0, columnspan=4, padx=5, pady=5)

    for i in range(7):
        window.grid_rowconfigure(i, weight=1)
    for i in range(4):
        window.grid_columnconfigure(i, weight=1)

    window.mainloop()


if __name__ == "__main__":
    start_calculator()

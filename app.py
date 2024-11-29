import tkinter as tk
from tkinter import ttk  # Для более современного стиля кнопок
from calc_oper import (
    addition, subtraction, multiplication, division, modulus, power,
    square_root, sine, cosine, floor_value, ceil_value,
)
from calc_oper import Memory

memory = Memory()
entry_text = None


def on_button_click(value):
    entry_text.set(entry_text.get() + value)


def on_clear():
    entry_text.set("")  # Очищает строку


def on_backspace():
    current_text = entry_text.get()
    entry_text.set(current_text[:-1])


def on_equal():
    try:
        expression = entry_text.get().replace("^", "**")
        result = eval(expression)
        entry_text.set(result)
    except ZeroDivisionError:
        entry_text.set("Error: Division by zero")
    except SyntaxError:
        entry_text.set("Error: Invalid syntax")
    except Exception as e:
        entry_text.set(f"Error: {e}")


def on_memory_add():
    try:
        value = float(entry_text.get())
        memory.m_add(value)
        entry_text.set("")
    except ValueError:
        entry_text.set("Error: Invalid input")


def on_memory_subtract():
    try:
        value = float(entry_text.get())
        memory.m_subtract(value)
        entry_text.set("")
    except ValueError:
        entry_text.set("Error: Invalid input")


def on_memory_recall():
    entry_text.set(str(memory.m_recall()))


def on_memory_clear():
    memory.m_clear()
    entry_text.set("")


def start_calculator():
    global entry_text
    window = tk.Tk()
    window.title("Calculator")
    window.geometry("400x600")
    window.configure(bg="#282c34")  # Устанавливаем темный фон

    entry_text = tk.StringVar()

    entry = tk.Entry(
        window, textvariable=entry_text, font=('Arial', 24),
        bd=10, relief="flat", justify="right", bg="#1e2227", fg="#ffffff"
    )
    entry.grid(row=0, column=0, columnspan=4, pady=(10, 20), padx=10, sticky="nsew")

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

    window.mainloop()


if __name__ == "__main__":
    start_calculator()

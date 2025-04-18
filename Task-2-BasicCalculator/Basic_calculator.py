

import tkinter as tk

def press(num):
    entry_text.set(entry_text.get() + str(num))


def equalpress():
    try:
        result = str(eval(entry_text.get()))
        entry_text.set(result)
    except:
        entry_text.set("Error")


def clear():
    entry_text.set("")


window = tk.Tk()
window.title("Reshma's basic Calculator")
window.geometry("300x420")
window.config(bg="pink")

entry_text = tk.StringVar()
entry = tk.Entry(window, textvariable=entry_text, font=('Arial', 18), bd=10, insertwidth=2, width=14, borderwidth=4)
entry.grid(row=0, column=0, columnspan=4,padx=10,pady=10)


# Buttons layout
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    action = lambda x=button: press(x) if x != "=" else equalpress()
    tk.Button(window, text=button, padx=20, pady=20, font=('Arial', 14),
              command=action).grid(row=row_val, column=col_val,padx=5,pady=5)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

tk.Button(window, text='C', padx=10, pady=20, font=('Arial', 14),bg="#ffa07a", command=clear).grid(row=row_val, column=0, columnspan=4, sticky='we',padx=5,pady=5)

window.mainloop()
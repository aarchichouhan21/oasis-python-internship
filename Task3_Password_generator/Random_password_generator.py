import tkinter as tk
import random
import string
def generate_password():
    try:
        length = int(length_entry.get())
    except:
        result_label.config(text="Enter valid length")
        strength_label.config(text="")
        return
    characters = ""
    if lower_var.get():
        characters += string.ascii_lowercase
    if upper_var.get():
        characters += string.ascii_uppercase
    if digit_var.get():
        characters += string.digits
    if symbol_var.get():
        characters += string.punctuation
    if characters == "":
        result_label.config(text="Select at least one option")
        strength_label.config(text="")
        return
    password = "".join(random.choice(characters) for _ in range(length))
    result_label.config(text=password)
    if length < 6:
        strength = "Weak"
    elif length < 10:
        strength = "Medium"
    else:
        strength = "Strong"
    strength_label.config(text="Strength: " + strength)
def copy_password():
    root.clipboard_clear()
    root.clipboard_append(result_label.cget("text"))
def save_password():
    password = result_label.cget("text")
    if password == "":
        result_label.config(text="No password to save")
        return
    with open("saved_passwords.txt", "a") as file:
        file.write(password + "\n")
    result_label.config(text="Password saved!")
root = tk.Tk()
root.title("Random Password Generator")
root.geometry("380x350")
title = tk.Label(root, text="Password Generator", font=("Arial", 16, "bold"))
title.pack(pady=10)
tk.Label(root, text="Password Length").pack()
length_entry = tk.Entry(root)
length_entry.pack()
lower_var = tk.IntVar()
upper_var = tk.IntVar()
digit_var = tk.IntVar()
symbol_var = tk.IntVar()
tk.Checkbutton(root, text="Lowercase Letters", variable=lower_var).pack()
tk.Checkbutton(root, text="Uppercase Letters", variable=upper_var).pack()
tk.Checkbutton(root, text="Numbers", variable=digit_var).pack()
tk.Checkbutton(root, text="Symbols", variable=symbol_var).pack()
generate_btn = tk.Button(root, text="Generate Password", command=generate_password)
generate_btn.pack(pady=10)
result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=5)
strength_label = tk.Label(root, text="", font=("Arial", 10))
strength_label.pack()
copy_btn = tk.Button(root, text="Copy Password", command=copy_password)
copy_btn.pack(pady=10)
save_btn = tk.Button(root, text="Save Password", command=save_password)
save_btn.pack(pady=5)
root.mainloop()
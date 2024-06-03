import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip

class PasswordGenerator:
    def __init__(self, master):
        self.master = master
        master.title("Password Generator")

        self.length_label = tk.Label(master, text="Password Length:")
        self.length_label.grid(row=0, column=0, sticky=tk.W)

        self.length_entry = tk.Entry(master)
        self.length_entry.grid(row=0, column=1)
        self.length_entry.insert(tk.END, "12")

        self.complexity_label = tk.Label(master, text="Password Complexity:")
        self.complexity_label.grid(row=1, column=0, sticky=tk.W)

        self.complexity_var = tk.StringVar(master)
        self.complexity_var.set("Medium")
        self.complexity_options = ["Low", "Medium", "High"]
        self.complexity_menu = tk.OptionMenu(master, self.complexity_var, *self.complexity_options)
        self.complexity_menu.grid(row=1, column=1, sticky=tk.W)

        self.generate_button = tk.Button(master, text="Generate Password", command=self.generate_password)
        self.generate_button.grid(row=2, column=0, columnspan=2)

        self.password_label = tk.Label(master, text="Generated Password:")
        self.password_label.grid(row=3, column=0, sticky=tk.W)

        self.password_entry = tk.Entry(master, state="readonly")
        self.password_entry.grid(row=3, column=1)

        self.copy_button = tk.Button(master, text="Copy to Clipboard", command=self.copy_to_clipboard)
        self.copy_button.grid(row=4, column=0, columnspan=2)

    def generate_password(self):
        length = int(self.length_entry.get())
        complexity = self.complexity_var.get()

        if complexity == "Low":
            chars = string.ascii_letters + string.digits
        elif complexity == "Medium":
            chars = string.ascii_letters + string.digits + string.punctuation
        else:
            chars = string.ascii_letters + string.digits + string.punctuation + string.ascii_uppercase

        generated_password = ''.join(random.choice(chars) for i in range(length))
        self.password_entry.config(state="normal")
        self.password_entry.delete(0, tk.END)
        self.password_entry.insert(0, generated_password)
        self.password_entry.config(state="readonly")

    def copy_to_clipboard(self):
        password = self.password_entry.get()
        pyperclip.copy(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")

root = tk.Tk()
my_password_generator = PasswordGenerator(root)
root.mainloop()


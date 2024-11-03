# import re

# def pwrds(password):
#     if len(password) < 8:
#         return "password too weak - too short"
#     if not re.search("[a-z]", password):
#         return "password too weak - no lowercase"
#     if not re.search("[A-Z]", password):
#         return "password too weak - no uppercase"
#     if not re.search("[0-9]", password):
#         return "password too weak - no digit"
#     if not re.search("[@#$%^&*]", password):
#         return "password too weak - no special character"
#     return "password is strong"
# password = input("Enter a password: ")
# strength = pwrds(password)
# print(strength)
import re
import tkinter as tk
from tkinter import messagebox

def pwrds(password):
    if len(password) < 8:
        return "password too weak - too short"
    if not re.search("[a-z]", password):
        return "password too weak - no lowercase"
    if not re.search("[A-Z]", password):
        return "password too weak - no uppercase"
    if not re.search("[0-9]", password):
        return "password too weak - no digit"
    if not re.search("[@#$%^&*]", password):
        return "password too weak - no special character"
    return "password is strong"

def check_password():
    password = entry.get()
    strength = pwrds(password)
    messagebox.showinfo("Password Strength", strength)

# Create the main window
root = tk.Tk()
root.title("Password Strength Checker")

# Create and place the widgets
tk.Label(root, text="Enter a password:").pack(pady=10)
entry = tk.Entry(root, show="*")
entry.pack(pady=5)

tk.Button(root, text="Check Strength", command=check_password).pack(pady=10)

# Run the application
root.mainloop()
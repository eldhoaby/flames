Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import tkinter as tk
from tkinter import messagebox

def flames_result(name1, name2):
    # Normalize input by removing spaces and converting to lowercase
    name1 = name1.lower().replace(" ", "")
    name2 = name2.lower().replace(" ", "")

    # Remove common letters
    for char in name1:
        if char in name2:
            name1 = name1.replace(char, "", 1)
            name2 = name2.replace(char, "", 1)

    # Calculate total remaining letters
    count = len(name1) + len(name2)

    # FLAMES Logic
...     flames = ["Friends", "Love", "Affection", "Marriage", "Enemies", "Siblings"]
...     while len(flames) > 1:
...         split_index = (count % len(flames)) - 1
...         if split_index >= 0:
...             flames = flames[split_index + 1:] + flames[:split_index]
...         else:
...             flames = flames[:len(flames) - 1]
... 
...     return flames[0]
... 
... def calculate_flames():
...     name1 = entry_name1.get()
...     name2 = entry_name2.get()
... 
...     if name1 and name2:
...         result = flames_result(name1, name2)
...         messagebox.showinfo("FLAMES Result", f"{name1} and {name2} are: {result}")
...     else:
...         messagebox.showwarning("Input Error", "Please enter both names.")
... 
... # Create GUI window
... root = tk.Tk()
... root.title("FLAMES Calculator")
... root.geometry("400x200")
... 
... # GUI Elements
... tk.Label(root, text="Enter First Name:").pack(pady=5)
... entry_name1 = tk.Entry(root)
... entry_name1.pack(pady=5)
... 
... tk.Label(root, text="Enter Second Name:").pack(pady=5)
... entry_name2 = tk.Entry(root)
... entry_name2.pack(pady=5)
... 
... calculate_button = tk.Button(root, text="Calculate FLAMES", command=calculate_flames)
... calculate_button.pack(pady=10)
... 

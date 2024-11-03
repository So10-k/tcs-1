import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
from tkinter.scrolledtext import ScrolledText
from tkinter import ttk  # Import ttk module
from PIL import Image, ImageTk

# Functionality for the drawing canvas
def clear_canvas():
    canvas.delete("all")

def draw(event):
    x, y = event.x, event.y
    canvas.create_oval(x-2, y-2, x+2, y+2, fill='black', outline='black')

# Functionality for the to-do list
def add_task():
    task = task_entry.get()
    if task != "":
        tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

def delete_task():
    try:
        selected_task_index = tasks_listbox.curselection()[0]
        tasks_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to delete.")

# Functionality for the calculator
def calculate():
    try:
        result = eval(calc_entry.get())
        calc_result_var.set(result)
    except Exception as e:
        calc_result_var.set("Error")

# Functionality for the text editor
def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, 'r') as file:
            text_editor.delete(1.0, tk.END)
            text_editor.insert(tk.END, file.read())

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, 'w') as file:
            file.write(text_editor.get(1.0, tk.END))

# Create the main window
root = tk.Tk()
root.title("Multi-Functional Tkinter App")
root.geometry("800x600")

# Create a notebook (tabbed interface)
notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill='both')

# Drawing Canvas Tab
canvas_tab = tk.Frame(notebook)
notebook.add(canvas_tab, text="Drawing Canvas")

canvas = tk.Canvas(canvas_tab, bg='white', width=600, height=400)
canvas.pack(pady=10)
canvas.bind("<B1-Motion>", draw)

clear_button = tk.Button(canvas_tab, text="Clear Canvas", command=clear_canvas)
clear_button.pack(pady=10)

# To-Do List Tab
todo_tab = tk.Frame(notebook)
notebook.add(todo_tab, text="To-Do List")

task_entry = tk.Entry(todo_tab, width=40)
task_entry.pack(pady=10)

add_task_button = tk.Button(todo_tab, text="Add Task", command=add_task)
add_task_button.pack(pady=5)

tasks_listbox = tk.Listbox(todo_tab, width=50, height=15)
tasks_listbox.pack(pady=10)

delete_task_button = tk.Button(todo_tab, text="Delete Task", command=delete_task)
delete_task_button.pack(pady=5)

# Calculator Tab
calc_tab = tk.Frame(notebook)
notebook.add(calc_tab, text="Calculator")

calc_entry = tk.Entry(calc_tab, width=20)
calc_entry.pack(pady=10)

calc_result_var = tk.StringVar()
calc_result_label = tk.Label(calc_tab, textvariable=calc_result_var)
calc_result_label.pack(pady=10)

calc_button = tk.Button(calc_tab, text="Calculate", command=calculate)
calc_button.pack(pady=10)

# Text Editor Tab
text_editor_tab = tk.Frame(notebook)
notebook.add(text_editor_tab, text="Text Editor")

text_editor = ScrolledText(text_editor_tab, wrap=tk.WORD, width=70, height=20)
text_editor.pack(pady=10)

open_button = tk.Button(text_editor_tab, text="Open File", command=open_file)
open_button.pack(side=tk.LEFT, padx=10)

save_button = tk.Button(text_editor_tab, text="Save File", command=save_file)
save_button.pack(side=tk.RIGHT, padx=10)

# Run the application
root.mainloop()
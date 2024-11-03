import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk, ImageChops
import numpy as np

def clear_canvas():
    canvas.delete("all")

def check_accuracy():
    # Save the user's drawing
    canvas.postscript(file="user_drawing.ps", colormode='color')
    user_image = Image.open("user_drawing.ps")
    user_image = user_image.resize((reference_image.width, reference_image.height), Image.Resampling.LANCZOS)
    
    # Convert images to grayscale
    ref_image_gray = reference_image.convert('L')
    user_image_gray = user_image.convert('L')
    
    # Calculate the difference
    diff = ImageChops.difference(ref_image_gray, user_image_gray)
    diff_array = np.array(diff)
    accuracy = 100 - (np.sum(diff_array) / (diff_array.size * 255) * 100)
    
    messagebox.showinfo("Accuracy", f"Your drawing accuracy is: {accuracy:.2f}%")

def draw(event):
    x, y = event.x, event.y
    canvas.create_oval(x-2, y-2, x+2, y+2, fill='black', outline='black')

# Create the main window
root = tk.Tk()
root.title("Drawing Mimic Game")
root.geometry("800x600")

# Load the reference image
reference_image_path = filedialog.askopenfilename(
    title="Select Reference Image", 
    filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp *.gif")]
)
if not reference_image_path:
    messagebox.showerror("Error", "No image selected. Exiting.")
    root.destroy()
else:
    reference_image = Image.open(reference_image_path)
    reference_image = reference_image.resize((400, 400), Image.Resampling.LANCZOS)
    reference_image_tk = ImageTk.PhotoImage(reference_image)

    # Create and place the widgets
    reference_label = tk.Label(root, image=reference_image_tk)
    reference_label.pack(side=tk.LEFT, padx=10, pady=10)

    canvas = tk.Canvas(root, bg='white', width=400, height=400)
    canvas.pack(side=tk.RIGHT, padx=10, pady=10)
    canvas.bind("<B1-Motion>", draw)

    button_frame = tk.Frame(root)
    button_frame.pack(side=tk.BOTTOM, pady=10)

    clear_button = tk.Button(button_frame, text="Clear", command=clear_canvas)
    clear_button.pack(side=tk.LEFT, padx=10)

    check_button = tk.Button(button_frame, text="Check Accuracy", command=check_accuracy)
    check_button.pack(side=tk.RIGHT, padx=10)

# Run the application
root.mainloop()
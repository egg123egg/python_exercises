import tkinter as tk
from tkinter import messagebox
import math

def calculate_area():
    try:
        radius = float(entry_radius.get())
        if radius < 0:
            raise ValueError("Radius cannot be negative.")
        area = math.pi * radius ** 2
        label_result.config(text=f"Area: {area:.2f}")
    except ValueError as e:
        messagebox.showerror("Invalid Input", f"Error: {e}")

def on_choice():
    choice = choice_var.get()
    messagebox.showinfo("Choice Selected", f"You selected: {choice}")

# Create the main window
window = tk.Tk()
window.title("Circle Area Calculator")
window.geometry("300x200")

# Create input label and entry
label_prompt = tk.Label(window, text="Enter the radius of the circle:")
label_prompt.pack(pady=10)

entry_radius = tk.Entry(window, width=20)
entry_radius.pack(pady=5)

# Create a button to calculate the area
button_calculate = tk.Button(window, text="Calculate Area", command=calculate_area)
button_calculate.pack(pady=10)

# Create a label to display the result
label_result = tk.Label(window, text="Area: ", font=("Arial", 12))
label_result.pack(pady=10)

# Create a label for choices
label_choice = tk.Label(window, text="Choose an option:")
label_choice.pack()

# Create a variable to store the selected choice
choice_var = tk.StringVar(value="Option 1")

# Create radio buttons for choices
radio1 = tk.Radiobutton(window, text="Option 1", variable=choice_var, value="Option 1")
radio1.pack()
radio2 = tk.Radiobutton(window, text="Option 2", variable=choice_var, value="Option 2")
radio2.pack()
radio3 = tk.Radiobutton(window, text="Option 3", variable=choice_var, value="Option 3")
radio3.pack()

# Create a button to confirm the choice
button_choice = tk.Button(window, text="Confirm Choice", command=on_choice)
button_choice.pack()

# Run the application
window.mainloop()

#In this code:Entry widgets are created for the user to input 7 numbers.A button is provided to generate the Joker number based on the last digit of each input number.The result is displayed in a label below the button.The ttkbootstrap style, background color, and font settings are applied to the widgets. #

import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style

def generate_joker_number():
    # Get the numbers from the entry widgets
    numbers = [int(entry.get()) for entry in entry_widgets]

    # Extract the last digit of each number and concatenate them to form the Joker number
    joker_number = ' '.join(str(num % 10) for num in numbers)

    # Display the Joker number
    result_label.config(text=f"Joker number is: {joker_number}", style='success.TLabel')

# Create the main Tkinter window
root = tk.Tk()
root.title("Joker Number Generator")
root.geometry("600x400")
root.configure(bg='#e6ffe6')  # Light green background color

# Apply ttkbootstrap style
style = Style(theme='minty')

# Create a frame to hold the widgets
frame = ttk.Frame(root)
frame.pack(padx=20, pady=20)

# Create labels and entry widgets for 7 numbers
entry_widgets = []
for row in range(7):
    label = ttk.Label(frame, text=f"Enter number {row+1}:", font=("Verdana", 12, "bold"))
    label.grid(row=row, column=0, padx=10, pady=5)
    entry = ttk.Entry(frame, style='success.TEntry', font=("Verdana", 12))
    entry.grid(row=row, column=1, padx=10, pady=5)
    entry_widgets.append(entry)

# Create a button to generate the Joker number
generate_button = ttk.Button(frame, text="Generate Joker Number", command=generate_joker_number, style='primary.TButton')
generate_button.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

# Create a label to display the result
result_label = ttk.Label(root, text="", style='success.TLabel')
result_label.pack(padx=20, pady=20)

# Start the Tkinter event loop
root.mainloop()



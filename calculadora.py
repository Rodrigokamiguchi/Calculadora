import tkinter as tk
from tkinter import messagebox

# Function for calculation
def calculate_expression(expression):
    try:
        result = eval(expression)
        return result
    except ZeroDivisionError:
        return "Error: Division by zero"
    except Exception:
        return "Error: Invalid expression"
    
# Function to update the display
def update_display(value):
    current = display_var.get()
    display_var.set(current + str(value))

# Function to clear the display
def clear_display():
    display_var.set("")

# Function to calculate the result
def show_result():
    expression = display_var.get()
    result = calculate_expression(expression)
    display_var.set(str(result))

# Function to create the calculator layout
def create_calculator():
    root = tk.Tk()
    root.title("Calculator")

    global display_var
    display_var = tk.StringVar()

    # Display where numbers and results will appear
    display = tk.Entry(root, textvariable=display_var, font=("Arial", 20), bd=10, insertwidth=2, width=14, borderwidth=4, justify="right")
    display.grid(row=0, column=0, columnspan=4)
    
    # List of buttons
    buttons = [
        '7', '8', '9', '/', 
        '4', '5', '6', '*', 
        '1', '2', '3', '-', 
        '0', '.', '=', '+'
    ]

    # Creating numeric and operation buttons
    row_val = 1
    col_val = 0
    for button in buttons:
        action = lambda x=button: update_display(x) if x != '=' else show_result()
        tk.Button(root, text=button, padx=20, pady=20, font=("Arial", 18), command=action).grid(row=row_val, column=col_val)
        col_val += 1
        if col_val > 3:
            col_val = 0
            row_val += 1

    # Button to clear the display
    tk.Button(root, text="C", padx=20, pady=20, font=("Arial", 18), command=clear_display).grid(row=row_val, column=0, columnspan=4, sticky="we")

    root.mainloop()

# Start the calculator
create_calculator()

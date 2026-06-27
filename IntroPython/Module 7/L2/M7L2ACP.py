from datetime import date
import tkinter as tk
from tkinter import messagebox

def calculate_age():
    """Calculates age based on user input and displays it."""
    try:
        # Get integers from the entry boxes
        day = int(entry_day.get())
        month = int(entry_month.get())
        year = int(entry_year.get())
        
        # Create date objects for birth date and today
        birth_date = date(year, month, day)
        today = date.today()
        
        # Calculate age
        age = today.year - birth_date.year
        
        # Adjust age if the birthday hasn't occurred yet this year
        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age -= 1
            
        # Display the result
        label_result.config(text=f"Present Age: {age} years old")
        
    except ValueError:
        # Triggers if inputs are empty, not numbers, or form an invalid date (e.g., Feb 30)
        messagebox.showerror("Error", "Please enter a valid day, month, and year.")

# Set up main window
root = tk.Tk()
root.title("Age Calculator")
root.geometry("300x250")

# Day Input
tk.Label(root, text="Day (DD):").pack(pady=2)
entry_day = tk.Entry(root, width=10)
entry_day.pack(pady=2)

# Month Input
tk.Label(root, text="Month (MM):").pack(pady=2)
entry_month = tk.Entry(root, width=10)
entry_month.pack(pady=2)

# Year Input
tk.Label(root, text="Year (YYYY):").pack(pady=2)
entry_year = tk.Entry(root, width=10)
entry_year.pack(pady=2)

# Calculate Button
btn_calculate = tk.Button(root, text="Calculate Age", command=calculate_age)
btn_calculate.pack(pady=15)

# Result Label
label_result = tk.Label(root, text="Present Age: ", font=("Arial", 11, "bold"))
label_result.pack(pady=5)

root.mainloop()

import tkinter as tk

def convert():
    # Convert input inches to cm (1 inch = 2.54 cm)
    cm = float(entry.get()) * 2.54
    lbl_res.config(text=f"Centimeters: {cm:.2f}")

root = tk.Tk()
root.title("Inches to CM")

# Input field
entry = tk.Entry(root)
entry.pack()

# Conversion button
btn = tk.Button(root, text="Convert", command=convert)
btn.pack()

# Result label
lbl_res = tk.Label(root, text="Centimeters: ")
lbl_res.pack()

root.mainloop()

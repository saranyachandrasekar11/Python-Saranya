import tkinter as tk

def calculate():
    # Fetch inputs and convert to float numbers
    p = float(entry_p.get())  # Principal
    t = float(entry_t.get())  # Time (years)
    r = float(entry_r.get())  # Rate of interest (%)

    # Calculations
    si = (p * t * r) / 100
    ci = p * ((1 + r / 100) ** t) - p

    # Update output labels
    lbl_si.config(text=f"Simple Interest: {si:.2f}")
    lbl_ci.config(text=f"Compound Interest: {ci:.2f}")

root = tk.Tk()
root.title("Interest Calculator")

# Input for Principal
entry_p = tk.Entry(root)
entry_p.pack()

# Input for Time
entry_t = tk.Entry(root)
entry_t.pack()

# Input for Rate
entry_r = tk.Entry(root)
entry_r.pack()

# Calculation button
btn = tk.Button(root, text="Calculate", command=calculate)
btn.pack()

# Result displays
lbl_si = tk.Label(root, text="Simple Interest: ")
lbl_si.pack()

lbl_ci = tk.Label(root, text="Compound Interest: ")
lbl_ci.pack()

root.mainloop()

import tkinter as tk

def multiply():
    # Fetch values, multiply them, and update the text
    ans = float(e1.get()) * float(e2.get())
    lbl_res.config(text=f"Result: {ans}")

root = tk.Tk()
root.title("Multiply")

# Inputs
e1 = tk.Entry(root)
e1.pack()

e2 = tk.Entry(root)
e2.pack()

# Button to trigger multiplication
btn = tk.Button(root, text="Multiply", command=multiply)
btn.pack()

# Label to show the final answer
lbl_res = tk.Label(root, text="Result: ")
lbl_res.pack()

root.mainloop()

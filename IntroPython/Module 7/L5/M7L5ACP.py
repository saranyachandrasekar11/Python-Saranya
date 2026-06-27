import tkinter as tk

def check_strength():
    # Get the password from the entry box
    password = entry.get()
    length = len(password)
    
    # Evaluate strength based on length
    if length == 0:
        lbl_res.config(text="Strength: Empty", fg="gray")
    elif length < 6:
        lbl_res.config(text="Strength: Weak (Too short)", fg="red")
    elif length <= 10:
        lbl_res.config(text="Strength: Medium", fg="orange")
    else:
        lbl_res.config(text="Strength: Strong", fg="green")

root = tk.Tk()
root.title("Password Strength")

# Password Input (show="*" hides the characters as you type)
entry = tk.Entry(root, show="*")
entry.pack(pady=5)

# Check Button
btn = tk.Button(root, text="Check Strength", command=check_strength)
btn.pack(pady=5)

# Strength Result Display
lbl_res = tk.Label(root, text="Strength: ", font=("Arial", 10, "bold"))
lbl_res.pack(pady=5)

root.mainloop()

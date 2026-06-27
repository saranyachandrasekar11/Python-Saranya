import tkinter as tk
import random

# Core game logic variables
user_score = 0
computer_score = 0
options = ["Rock", "Paper", "Scissors"]

# Function to handle the game logic when a user clicks a choice
def play_round(user_choice):
    global user_score, computer_score
    
    # 1. Computer makes a random choice
    computer_choice = random.choice(options)
    
    # 2. Determine the winner
    if user_choice == computer_choice:
        result_text = f"It's a Tie! Both chose {user_choice}."
        result_color = "#333333"  # Neutral dark gray
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result_text = f"You Win! {user_choice} beats {computer_choice}."
        result_color = "#2e7d32"  # Success green
        user_score += 1
    else:
        result_text = f"You Lose! {computer_choice} beats {user_choice}."
        result_color = "#c62828"  # Error red
        computer_score += 1

    # 3. Update the GUI components with current data
    user_choice_label.config(text=f"Your Choice: {user_choice}")
    comp_choice_label.config(text=f"Computer's Choice: {computer_choice}")
    result_label.config(text=result_text, fg=result_color)
    score_label.config(text=f"Score - You: {user_score} | Computer: {computer_score}")

# Function to reset scores and status message labels back to default
def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    
    user_choice_label.config(text="Your Choice: None")
    comp_choice_label.config(text="Computer's Choice: None")
    result_label.config(text="Make your move to start!", fg="#555555")
    score_label.config(text="Score - You: 0 | Computer: 0")

# --- GUI Setup Layout ---
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("450x450")
root.configure(bg="#f4f4f9")

# Header title banner layout
title_label = tk.Label(
    root, text="Rock Paper Scissors", font=("Helvetica", 22, "bold"), 
    bg="#3f51b5", fg="white", pady=10
)
title_label.pack(fill=tk.X)

# Running score tracking area
score_label = tk.Label(
    root, text="Score - You: 0 | Computer: 0", font=("Helvetica", 14, "bold"), 
    bg="#f4f4f9", fg="#333333", pady=15
)
score_label.pack()

# Container frame holding game activity selection state displays
display_frame = tk.Frame(root, bg="#f4f4f9")
display_frame.pack(pady=10)

user_choice_label = tk.Label(display_frame, text="Your Choice: None", font=("Helvetica", 12), bg="#f4f4f9", fg="#555555")
user_choice_label.pack(anchor="w")

comp_choice_label = tk.Label(display_frame, text="Computer's Choice: None", font=("Helvetica", 12), bg="#f4f4f9", fg="#555555")
comp_choice_label.pack(anchor="w", pady=5)

# Round conclusion context banner layout
result_label = tk.Label(
    root, text="Make your move to start!", font=("Helvetica", 14, "italic"), 
    bg="#f4f4f9", fg="#555555", pady=20
)
result_label.pack()

# Interactive user choices button navigation structure
btn_frame = tk.Frame(root, bg="#f4f4f9")
btn_frame.pack(pady=10)

rock_btn = tk.Button(btn_frame, text="✊ Rock", font=("Helvetica", 12, "bold"), width=10, bg="#e0e0e0", command=lambda: play_round("Rock"))
rock_btn.grid(row=0, column=0, padx=10)

paper_btn = tk.Button(btn_frame, text="✋ Paper", font=("Helvetica", 12, "bold"), width=10, bg="#e0e0e0", command=lambda: play_round("Paper"))
paper_btn.grid(row=0, column=1, padx=10)

scissors_btn = tk.Button(btn_frame, text="✌️ Scissors", font=("Helvetica", 12, "bold"), width=10, bg="#e0e0e0", command=lambda: play_round("Scissors"))
scissors_btn.grid(row=0, column=2, padx=10)

# Dashboard global refresh operation layout execution
reset_btn = tk.Button(
    root, text="Reset Game", font=("Helvetica", 11, "bold"), 
    bg="#757575", fg="white", activebackground="#616161", activeforeground="white",
    command=reset_game, padx=10, pady=5
)
reset_btn.pack(pady=25)

# Initialize application cycle interface
root.mainloop()

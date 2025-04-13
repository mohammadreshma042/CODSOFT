import tkinter as tk
import random

choices = ["Rock", "Paper", "Scissors"]


user_score = 0
computer_score = 0
player1_score = 0
player2_score = 0


player1_choice = ""

def reset_scores():
    global user_score, computer_score, player1_score, player2_score, player1_choice
    user_score = 0
    computer_score = 0
    player1_score = 0
    player2_score = 0
    player1_choice = ""
    update_score_label()

def update_score_label():
    mode = mode_var.get()
    if mode == "single":
        score_label.config(text=f"Score: You {user_score} - {computer_score} Computer")
    else:
        score_label.config(text=f"Score: P1 ({player1_score}) - ({player2_score}) P2")

def play(user_choice):
    global user_score, computer_score, player1_score, player2_score, player1_choice

    mode = mode_var.get()
    if mode == "single":
        # Single Mode: user vs computer
        computer_choice = random.choice(choices)

        if user_choice == computer_choice:
            result = "It's a Tie!"
            color = "#FFA500"
        elif (user_choice == "Rock" and computer_choice == "Scissors") or \
             (user_choice == "Paper" and computer_choice == "Rock") or \
             (user_choice == "Scissors" and computer_choice == "Paper"):
            result = "You Win!"
            user_score += 1
            color = "#32CD32"
        else:
            result = "Computer Wins!"
            computer_score += 1
            color = "#FF6347"

        result_label.config(
            text=f"You chose: {user_choice}\nComputer chose: {computer_choice}\n{result}",
            fg=color
        )
        update_score_label()
    else:
       
        if player1_choice == "":
            # First player's turn
            player1_choice = user_choice
            result_label.config(
                text=f"Player 1 chose: {player1_choice}\nNow it's Player 2's turn.",
                fg="#1E90FF"
            )
        else:
            
            player2_choice = user_choice
            if player1_choice == player2_choice:
                result = "It's a Tie!"
                color = "#FFA500"
            elif (player1_choice == "Rock" and player2_choice == "Scissors") or \
                 (player1_choice == "Paper" and player2_choice == "Rock") or \
                 (player1_choice == "Scissors" and player2_choice == "Paper"):
                result = "Player 1 Wins!"
                player1_score += 1
                color = "#32CD32"
            else:
                result = "Player 2 Wins!"
                player2_score += 1
                color = "#FF6347"
            result_label.config(
                text=f"Player 1 chose: {player1_choice}\nPlayer 2 chose: {player2_choice}\n{result}",
                fg=color
            )
            player1_choice = ""  
            update_score_label()

def change_mode():
    
    reset_scores()
    if mode_var.get() == "single":
        instruction_label.config(text="Single Mode: Choose Rock, Paper, or Scissors (or press corresponding keys)")
    else:
        instruction_label.config(text="2 Players Mode: Player 1: Choose Rock, Paper, or Scissors (or press keys)")


root = tk.Tk()
root.title("Rock Paper Scissors - CodSoft Internship Task 4")
root.geometry("420x450")
root.config(bg="#e6f2ff")

tk.Label(
    root, text="Rock Paper Scissors Game", 
    font=("Helvetica", 20, "bold"), bg="#e6f2ff", fg="#333"
).pack(pady=10)


mode_var = tk.StringVar(value="single")
mode_frame = tk.Frame(root, bg="#e6f2ff")
mode_frame.pack(pady=5)
tk.Radiobutton(mode_frame, text="Single Mode", variable=mode_var, value="single",
               font=("Helvetica", 12), bg="#e6f2ff", command=change_mode).pack(side="left", padx=10)
tk.Radiobutton(mode_frame, text="2 Players Mode", variable=mode_var, value="2players",
               font=("Helvetica", 12), bg="#e6f2ff", command=change_mode).pack(side="left", padx=10)


instruction_label = tk.Label(root, text="Single Mode: Choose Rock, Paper, or Scissors (or press corresponding keys)",
                             font=("Helvetica", 12), bg="#e6f2ff", fg="#333")
instruction_label.pack(pady=5)

# Frame for buttons
button_frame = tk.Frame(root, bg="#e6f2ff")
button_frame.pack(pady=10)
style = {
    "font": ("Helvetica", 12, "bold"),
    "width": 12,
    "height": 2,
    "bd": 0,
    "relief": "solid",
    "activebackground": "#d1e0e0"
}
tk.Button(button_frame, text="Rock", bg="#FF9999", command=lambda: play("Rock"), **style).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="Paper", bg="#99CCFF", command=lambda: play("Paper"), **style).grid(row=0, column=1, padx=5)
tk.Button(button_frame, text="Scissors", bg="#99FF99", command=lambda: play("Scissors"), **style).grid(row=0, column=2, padx=5)

# Result label
result_label = tk.Label(root, text="", font=("Helvetica", 14), bg="#e6f2ff")
result_label.pack(pady=20)

# Score label
score_label = tk.Label(root, text="Score: You 0 - 0 Computer", font=("Helvetica", 13), bg="#e6f2ff", fg="#333")
score_label.pack()

# Exit button
tk.Button(
    root, text="Exit", font=("Helvetica", 10, "bold"), bg="#FF6666", fg="white", width=10,
    command=root.quit
).pack(pady=15)

# Bind keys for quick play (r, p, s)
def key_handler(event):
    key = event.char.lower()
    if key == "r":
        play("Rock")
    elif key == "p":
        play("Paper")
    elif key == "s":
        play("Scissors")

root.bind("<Key>", key_handler)

# Start the main loop
root.mainloop()

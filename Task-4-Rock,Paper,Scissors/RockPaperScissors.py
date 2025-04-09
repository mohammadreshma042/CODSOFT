import tkinter as tk
import random
choices = ["Rock", "Paper", "Scissors"]
user_score = 0
computer_score = 0
def play(user_choice):
    global user_score, computer_score

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
    score_label.config(text=f"Score: You {user_score} - {computer_score} Computer")
root = tk.Tk()
root.title("Rock Paper Scissors - CodSoft Internship Task 4")
root.geometry("420x400")
root.config(bg="#e6f2ff")
tk.Label(
    root, text="Rock Paper Scissors Game", 
    font=("Helvetica", 20, "bold"), bg="#e6f2ff", fg="#333"
).pack(pady=20)

button_frame = tk.Frame(root, bg="#e6f2ff")
button_frame.pack()
style = {
    "font": ("Helvetica", 12, "bold"),
    "width": 12,
    "height": 2,
    "bd": 0,
    "relief": "solid",
    "activebackground": "#d1e0e0"
}
tk.Button(button_frame, text="Rock", bg="#FF9999", command=lambda: play("Rock"), **style).grid(row=0, column=0, padx=10)
tk.Button(button_frame, text="Paper", bg="#99CCFF", command=lambda: play("Paper"), **style).grid(row=0, column=1, padx=10)
tk.Button(button_frame, text="Scissors", bg="#99FF99", command=lambda: play("Scissors"), **style).grid(row=0, column=2, padx=10)
result_label = tk.Label(root, text="", font=("Helvetica", 14), bg="#e6f2ff")
result_label.pack(pady=25)
score_label = tk.Label(root, text="Score: You 0 - 0 Computer", font=("Helvetica", 13), bg="#e6f2ff", fg="#333")
score_label.pack()
tk.Button(
    root, text="Exit", font=("Helvetica", 10, "bold"), bg="#FF6666", fg="white", width=10,
    command=root.quit
).pack(pady=15)
root.mainloop()
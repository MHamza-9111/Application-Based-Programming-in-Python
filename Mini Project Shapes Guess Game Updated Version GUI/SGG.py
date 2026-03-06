# Modules
import random as r
import tkinter as tk

# Game Data
shapes = ["circle","square","rectangle","oval","diamond"]
attempts = 0
ai = r.choice(shapes)

# Guess Function
def guess():
    global attempts

    user = entry.get().lower()

    if user not in shapes:
        result.config(text="Invalid input!\nPlease enter [circle, square, rectangle, oval, diamond]")
        return

    attempts += 1

    if user == ai:
        result.config(text="Congrats! You Won!")

    elif attempts == 3:
        result.config(text=f"You Lose! The Shape Was {ai}")

    else:
        result.config(text=f"Wrong guess! Attempts left: {3-attempts}")

# Play Again Function
def play_again():
    global attempts, ai

    attempts = 0
    ai = r.choice(shapes)

    entry.delete(0, tk.END)
    result.config(text="Game restarted! Guess the shape.")

# Window
root = tk.Tk()
root.title("Shapes Guess Game")
root.geometry("500x300")
root.config(bg="orange")

# Heading
heading = tk.Label(
    root,
    text="Shapes Guess Game",
    font=("Bebas Nue", 18, "bold"),
    bg="orange"
)
heading.pack(pady=(30,0))

# Description
description = tk.Label(root, text="By Mohammad Hamza Mughal", font=("Bebas Nue", 10))
description.pack(pady=(0,20))

# Frame for Label & Textbox
frame = tk.Frame(root, padx=10, pady=10)
frame.pack(pady=10)

# Textbox Label
entry_text = tk.Label(frame, text="Enter Shape:", font=("Bebas Nue", 10, "bold"))
entry_text.pack(side="left", padx=5)

# Textbox
entry = tk.Entry(frame, font=("Arial", 14))
entry.pack(side="left")

# Guess Button
guess_button = tk.Button(frame, text="Guess", command=guess)
guess_button.pack(side="left", pady=10)

# Play Again Button
again_btn = tk.Button(root, text="Play Again", command=play_again)
again_btn.pack(pady=5)

# Result
result = tk.Label(
    root,
    text="You have 3 attempts",
    font=("Arial", 12, "bold"),
    bg="navy",
    fg="white",
    padx=10,
    pady=10
)
result.pack(pady=10)

# Window Loop
root.mainloop()
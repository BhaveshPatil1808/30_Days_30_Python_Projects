from tkinter import *
import random

# Function to randomly select computer's choice
def random_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

# Function to determine the result
def result(human_choice, comp_choice):
    global user_score, comp_score

    if human_choice == comp_choice:
        result_var.set(f"Both chose {human_choice}. It's a tie!")
    elif (human_choice == "rock" and comp_choice == "scissors") or \
         (human_choice == "paper" and comp_choice == "rock") or \
         (human_choice == "scissors" and comp_choice == "paper"):
        user_score += 1
        result_var.set(f"You chose {human_choice}, computer chose {comp_choice}. You win!")
    else:
        comp_score += 1
        result_var.set(f"You chose {human_choice}, computer chose {comp_choice}. Computer wins!")

    score_var.set(f"Score - You: {user_score} | Computer: {comp_score}")

# Handlers for each button
def rock():
    result("rock", random_computer_choice())

def paper():
    result("paper", random_computer_choice())

def scissors():
    result("scissors", random_computer_choice())

# Create the main window
rps = Tk()
rps.geometry("400x300")
rps.title("Rock Paper Scissors")

# Score variables
user_score = 0
comp_score = 0

# Tkinter StringVars for displaying results and scores
result_var = StringVar()
score_var = StringVar()
score_var.set("Score - You: 0 | Computer: 0")

# Buttons
button_rock = Button(rps, text="Rock", bg="#888487", font=("arial", 15, "italic bold"),
                     relief=RIDGE, activebackground="#059458", activeforeground="white",
                     width=24, command=rock)
button_rock.pack(pady=5)

button_paper = Button(rps, text="Paper", bg="#808487", font=("arial", 15, "italic bold"),
                      relief=RIDGE, activebackground="#85945B", activeforeground="white",
                      width=24, command=paper)
button_paper.pack(pady=5)

button_scissors = Button(rps, text="Scissors", bg="#808487", font=("arial", 15, "italic bold"),
                         relief=RIDGE, activebackground="#059458", activeforeground="white",
                         width=24, command=scissors)
button_scissors.pack(pady=5)

# Result and Score Labels
Label(rps, textvariable=result_var, font=("arial", 12)).pack(pady=10)
Label(rps, textvariable=score_var, font=("arial", 12, "bold")).pack(pady=10)

# Start the GUI loop
rps.mainloop()

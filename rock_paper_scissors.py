print("----------------------------------------------")
# --------------------- Rock Paper Scissor ---------------------
# --------------------------------------------------------------

import random

options = ("rock", "paper", "scissors")
running = True

while running:
    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter (rock, paper, scissors): ").lower()

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("Tie!")
    elif player == "rock" and computer == "scissors":
        print("You win!")
    elif player == "scissors" and computer == "paper":
        print("You win!")
    elif player == "paper" and computer == "rock":
        print("You win!")
    else:
        print("You lose!")

    if not input("Play Again (y/n): ").lower() == "y":
        running = False

print("Thanks for playing!")
input("Play Again (y/n): ").lower()

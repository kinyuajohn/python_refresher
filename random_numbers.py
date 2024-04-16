print("----------------------------------------------")
# --------------------- Generate Random Numbers ---------------------
# -------------------------------------------------------------------
import random

# options = ("rock", "paper", "scissors")
# cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

# # number = random.randint(1, 6) # 1, 2, 3, 4, 5, 6
# # number = random.random()  # 0 - 1
# # option = random.choice(options)
# random.shuffle(cards)

# print(cards)

# --------------------- Number Gueesing Game ---------------------
low = 1
high = 100
guesses = 0
number = random.randint(low, high)
# print(number)

while True:
    guess = int(input(f"Enter a number between ({low} - {high}): "))
    guesses += 1

    if guess < number:
        print("warmer -->")
    elif guess > number:
        print("colder <--")
    else:
        print("Correct")
        break

if guesses == 1:
    print("You guessed once! 👏👏👏")
else:
    print(f"You guessed {guesses} times.")

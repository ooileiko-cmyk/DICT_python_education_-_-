user_choice = input()

if user_choice == "rock":
    computer_choice = "paper"
elif user_choice == "paper":
    computer_choice = "scissors"
elif user_choice == "scissors":
    computer_choice = "rock"

print(f"Sorry, but the computer chose {computer_choice}")
import random

options = ["rock", "paper", "scissors"]

user_choice = input()
computer_choice = random.choice(options)

if user_choice == computer_choice:
    print(f"There is a draw ({computer_choice})")
elif (user_choice == "rock" and computer_choice == "scissors") or \
     (user_choice == "paper" and computer_choice == "rock") or \
     (user_choice == "scissors" and computer_choice == "paper"):
    print(f"Well done. The computer chose {computer_choice} and failed")
else:
    print(f"Sorry, but the computer chose {computer_choice}")
import random

options = ["rock", "paper", "scissors"]

while True:
    user_choice = input()

    if user_choice == "!exit":
        print("Bye!")
        break

    if user_choice not in options:
        print("Invalid input")
        continue

    computer_choice = random.choice(options)

    if user_choice == computer_choice:
        print(f"There is a draw ({computer_choice})")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print(f"Well done. The computer chose {computer_choice} and failed")
    else:
        print(f"Sorry, but the computer chose {computer_choice}")

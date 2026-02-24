user_choice = input()

if user_choice == "rock":
    computer_choice = "paper"
elif user_choice == "paper":
    computer_choice = "scissors"
elif user_choice == "scissors":
    computer_choice = "rock"

print(f"Sorry, but the computer chose {computer_choice}")
import random

while True:
    pencils = input("How many pencils would you like to use:\n> ")
    if not pencils.isdigit():
        print("The number of pencils should be numeric")
        continue
    pencils = int(pencils)
    if pencils <= 0:
        print("The number of pencils should be positive")
        continue
    break

user = "John"
bot = "Jack"

while True:
    first = input(f"Who will be the first ({user}, {bot}):\n> ")
    if first != user and first != bot:
        print(f"Choose between '{user}' and '{bot}'")
        continue
    break

print("|" * pencils)
print(f"{first} is going first!")

current = first


def bot_move(pencils_left):
    if pencils_left % 4 == 1:

        return random.choice([1, 2, 3])
    elif pencils_left % 4 == 0:
        return 3
    elif pencils_left % 4 == 3:
        return 2
    elif pencils_left % 4 == 2:
        return 1


while pencils > 0:
    print("|" * pencils)
    print(f"{current}'s turn:")

    if current == user:

        while True:
            move = input("> ")
            if move not in ["1", "2", "3"]:
                print("Possible values: '1', '2' or '3'")
                continue
            move = int(move)
            if move > pencils:
                print("Too many pencils were taken")
                continue
            break
    else:
        move = bot_move(pencils)
        print(move)

    pencils -= move

    if pencils == 0:
        winner = bot if current == user else user
        print(f"{winner} won!")
        break

    current = bot if current == user else user
pencils = input("How many pencils would you like to use:\n> ")

pencils = int(pencils)

user = "John"
bot = "Jack"

first = input(f"Who will be the first ({user}, {bot}):\n> ")

print("|" * pencils)
print(f"{first} is going first!")

current = first

while pencils > 0:
    print("|" * pencils)
    print(f"{current}'s turn:")

    while True:
        take = input("> ")

        if take not in ["1", "2", "3"]:
            print("Possible values: '1', '2' or '3'")
            continue

        take = int(take)

        if take > pencils:
            print("Too many pencils were taken")
            continue

        break

    pencils -= take

    if pencils == 0:
        winner = bot if current == user else user
        print(f"{winner} won!")
        break

    current = bot if current == user else user
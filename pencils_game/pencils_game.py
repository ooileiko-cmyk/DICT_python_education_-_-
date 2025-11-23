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

    taken = int(input("> "))

    pencils -= taken

    if pencils == 0:
        break

    current = bot if current == user else user
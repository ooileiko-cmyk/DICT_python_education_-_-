import random

num_friends = int(input("Enter number of friends joining (including you): > "))
if num_friends <= 0:
    print("No one is joining for the party")
    friends = {}
else:
    friends = {}
    print("Enter the name of every friend (including you), each on a new line:")
    for _ in range(num_friends):
        name = input("> ")
        friends[name] = 0
    print(friends)

if friends:
    total_amount = float(input("Enter the total amount: > "))
    share = round(total_amount / num_friends, 2)
    for name in friends:
        friends[name] = share
    print(friends)

total_amount = 0
lucky_choice = None
lucky_person = None

if friends:
    lucky_choice = input('Do you want to use the "Who is lucky?" feature? Write Yes/No: > ').strip()
    if lucky_choice.lower() == "yes":
        lucky_person = random.choice(list(friends.keys()))
        print(f"{lucky_person} is the lucky one!")
    else:
        print("No one is going to be lucky")
        lucky_person = None

if friends and lucky_choice.lower() == "yes":
    num_to_pay = len(friends) - 1
    if num_to_pay > 0:
        new_share = round(total_amount / num_to_pay, 2)
    else:
        new_share = 0
    for name in friends:
        if name == lucky_person:
            friends[name] = 0
        else:
            friends[name] = new_share
    print(friends)
import sqlite3
import random

# --- DB ---
conn = sqlite3.connect('card.s3db')
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS card (
    id INTEGER PRIMARY KEY,
    number TEXT,
    pin TEXT,
    balance INTEGER DEFAULT 0
);
""")
conn.commit()


# --- Luhn ---
def luhn_checksum(number):
    digits = [int(x) for x in number]
    for i in range(0, len(digits), 2):
        digits[i] *= 2
        if digits[i] > 9:
            digits[i] -= 9
    return sum(digits)


def generate_card_number():
    bin_number = "400000"
    account = str(random.randint(100000000, 999999999))
    partial = bin_number + account

    checksum = luhn_checksum(partial + "0")
    check_digit = (10 - (checksum % 10)) % 10

    return partial + str(check_digit)


def generate_pin():
    return str(random.randint(0, 9999)).zfill(4)


def create_account():
    number = generate_card_number()
    pin = generate_pin()

    cur.execute("INSERT INTO card (number, pin) VALUES (?, ?)", (number, pin))
    conn.commit()

    print("\nYour card has been created")
    print("Your card number:")
    print(number)
    print("Your card PIN:")
    print(pin)


def login():
    number = input("Enter your card number:\n")
    pin = input("Enter your PIN:\n")

    cur.execute("SELECT * FROM card WHERE number=? AND pin=?", (number, pin))
    account = cur.fetchone()

    if account:
        print("\nYou have successfully logged in!\n")
        account_menu(number)
    else:
        print("\nWrong card number or PIN!\n")


def get_balance(number):
    cur.execute("SELECT balance FROM card WHERE number=?", (number,))
    return cur.fetchone()[0]


def add_income(number):
    income = int(input("Enter income:\n"))
    cur.execute("UPDATE card SET balance = balance + ? WHERE number=?", (income, number))
    conn.commit()
    print("Income was added!")


def luhn_valid(card):
    return luhn_checksum(card) % 10 == 0


def transfer(number):
    print("Transfer")
    target = input("Enter card number:\n")

    if target == number:
        print("You can't transfer money to the same account!")
        return

    if not luhn_valid(target):
        print("Probably you made a mistake in the card number. Please try again!")
        return

    cur.execute("SELECT * FROM card WHERE number=?", (target,))
    if not cur.fetchone():
        print("Such a card does not exist.")
        return

    amount = int(input("Enter how much money you want to transfer:\n"))

    balance = get_balance(number)
    if balance < amount:
        print("Not enough money!")
        return

    cur.execute("UPDATE card SET balance = balance - ? WHERE number=?", (amount, number))
    cur.execute("UPDATE card SET balance = balance + ? WHERE number=?", (amount, target))
    conn.commit()

    print("Success!")


def close_account(number):
    cur.execute("DELETE FROM card WHERE number=?", (number,))
    conn.commit()
    print("The account has been closed!")


def account_menu(number):
    while True:
        print("""
1. Balance
2. Add income
3. Do transfer
4. Close account
5. Log out
0. Exit
""")

        choice = input()

        if choice == "1":
            print("Balance:", get_balance(number))
        elif choice == "2":
            add_income(number)
        elif choice == "3":
            transfer(number)
        elif choice == "4":
            close_account(number)
            break
        elif choice == "5":
            print("You have successfully logged out!")
            break
        elif choice == "0":
            print("Bye!")
            exit()


# --- MAIN ---
while True:
    print("""
1. Create an account
2. Log into account
0. Exit
""")

    choice = input()

    if choice == "1":
        create_account()
    elif choice == "2":
        login()
    elif choice == "0":
        print("Bye!")
        break
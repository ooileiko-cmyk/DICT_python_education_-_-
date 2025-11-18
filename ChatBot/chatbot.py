bot_name="Logas_bot"
birth_year=2026

print(f"Hello! My name is {bot_name}.")
print(f"I was created in {birth_year}.")

print("Please, remind me your name.")
your_name=input()
print(f"What a great name you have, {your_name}!")

print("Let me guess your age.")
print("Enter remainders dividing your age by 3, 5 and 7.")

remainder3=int(input())
remainder5=int(input())
remainder7=int(input())

your_age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
print(f"Your age is {your_age}; what a good time to start programming!")
print("Now I will prove to you that I can count to any number you want.")
num = int(input())
for i in range(num + 1):
    print(f"{i}!")

    print("Let's test your programming knowledge.")
    print("Why do we use methods?")
    print("1. To repeat code multiple times.")
    print("2. To divide a program into small subroutines.")
    print("3. To measure execution time of a program.")
    print("4. To turn off program execution.")

    while True:
        answer=input()
        if answer == "2":
            break
        else:
            print("Please, try again.")
            print("Congratulations, have a nice day!")
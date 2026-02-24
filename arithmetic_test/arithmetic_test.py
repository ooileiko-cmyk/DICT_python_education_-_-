import random

# Генерация задания
num1 = random.randint(2, 9)
num2 = random.randint(2, 9)
operation = random.choice(["+", "-", "*"])

question = f"{num1} {operation} {num2}"
print(question)

# Ответ пользователя
user_answer = input("> ")

# Проверка ответа
try:
    if int(user_answer) == eval(question):
        print("Right!")
    else:
        print("Wrong!")
except ValueError:
    print("Incorrect format")
    import random

    score = 0

    for _ in range(5):
        num1 = random.randint(2, 9)
        num2 = random.randint(2, 9)
        operation = random.choice(["+", "-", "*"])
        question = f"{num1} {operation} {num2}"

        while True:
            print(question)
            user_input = input("> ")
            try:
                user_answer = int(user_input)
                break
            except ValueError:
                print("Incorrect format.")

        if user_answer == eval(question):
            print("Right!")
            score += 1
        else:
            print("Wrong!")

    print(f"Your mark is {score}/5.")
    import random


    def get_level():
        while True:
            print("Which level do you want? Enter a number:")
            print("1 - simple operations with numbers 2-9")
            print("2 - integral squares of 11-29")
            level = input()
            if level in ("1", "2"):
                return int(level)
            print("Incorrect format.")


    def generate_task(level):
        if level == 1:
            num1 = random.randint(2, 9)
            num2 = random.randint(2, 9)
            operation = random.choice(["+", "-", "*"])
            question = f"{num1} {operation} {num2}"
            answer = eval(question)
            return question, answer
        else:
            num = random.randint(11, 29)
            question = f"{num}"
            answer = num ** 2
            return question, answer


    def get_answer():
        while True:
            user_input = input("> ")
            try:
                return int(user_input)
            except ValueError:
                print("Incorrect format.")


    def save_result(name, score, level):
        level_description = {
            1: "simple operations with numbers 2-9",
            2: "integral squares of 11-29"
        }
        with open("results.txt", "a") as file:
            file.write(f"{name}: {score}/5 in level {level} ({level_description[level]})\n")


    def main():
        level = get_level()
        score = 0

        for _ in range(5):
            question, correct_answer = generate_task(level)
            print(question)
            user_answer = get_answer()
            if user_answer == correct_answer:
                print("Right!")
                score += 1
            else:
                print("Wrong!")

        print(f"Your mark is {score}/5.")

        print("Would you like to save your result to the file? Enter yes or no.")
        save = input().lower()

        if save in ("yes", "y", "yeah", "yes"):
            print("What is your name?")
            name = input()
            save_result(name, score, level)


    if name == "main":
        main()
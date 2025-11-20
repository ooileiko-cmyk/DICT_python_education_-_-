import random

print("HANGMAN")
print("The game will be available soon.")

words = ["python", "java", "javascript", "php"]
secret_word =random.choice(words)

guess_word = input("Guess the word: > ")
if guess_word == secret_word:
    print("You survived!")
else:
    print("You lost!")

    display_word = secret_word[:3] + "-" * (len(secret_word) - 3)
    print("Guess the word:", display_word)

    guess_letter = input("Input a letter: > ")
    if guess_letter in secret_word:
        print("Correct!")
    else:
        print("That letter doesn't appear in the word")
    attempts = 8
    guessed_letters = set()

    while attempts > 0 and "-" in display_word:
        guess_letter = input("Input a letter: > ")

        if len(guess_letter) != 1:
            print("You should input a single letter")
            continue

        if not guess_letter.islower() or not guess_letter.isalpha():
            print("Please enter a lowercase English letter")
            continue

        if guess_letter in guessed_letters:
            print("You've already guessed this letter")
            continue

        guessed_letters.add(guess_letter)

        if guess_letter in secret_word:

            display_word = "".join(
                [c if c == guess_letter or c in guessed_letters or i < 3 else "-"
                 for i, c in enumerate(secret_word)])

            print(display_word)
        else:
            print("That letter doesn't appear in the word")
            attempts -= 1
            print(f"Attempts left: {attempts}")

    if "-" not in display_word:
        print(f"You guessed the word {secret_word}! You survived!")
    else:
        print("You lost!")
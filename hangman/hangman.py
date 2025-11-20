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
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
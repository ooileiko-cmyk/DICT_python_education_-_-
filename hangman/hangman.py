print("HANGMAN")
print("The game will be available soon.")
print("HANGMAN")

secret_word = "python"

guess = input("Guess the word: > ")

if guess == secret_word:
    print("You survived!")
else:
    print("You lost!")
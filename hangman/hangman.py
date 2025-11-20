import random

def play_game():
    print("HANGMAN")

    words = ["python", "java", "javascript", "php"]
    secret_word = random.choice(words)
    display_word = "-" * len(secret_word)
    attempts = 8
    guessed_letters = set()

    while attempts > 0 and display_word != secret_word:
        print(display_word)
        guess = input("Input a letter: > ")

        if len(guess) != 1:
            print("Please, input a single letter.")
            continue
        if not guess.isalpha() or not guess.islower():
            print("Please, enter a lowercase letter from the English alphabet.")
            continue
        if guess in guessed_letters:
            print("You've already guessed this letter.")
            continue

        guessed_letters.add(guess)

        if guess in secret_word:
            new_display = ""
            for i in range(len(secret_word)):
                if secret_word[i] == guess:
                    new_display += guess
                else:
                    new_display += display_word[i]
            display_word = new_display
        else:
            print("That letter doesn't appear in the word")
            attempts -= 1

    if display_word == secret_word:
        print(f"You guessed the word {secret_word}!")
        print("You survived!")
    else:
        print("You lost!")


print("HANGMAN")
while True:
    choice = input('Type "play" to play the game, "exit" to quit: > ').strip()

    if choice == "play":
        play_game()
    elif choice == "exit":
        break
    else:
        continue

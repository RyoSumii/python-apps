import termcolor
from hangman_words import word_list
from hangman_art import stages, logo, cong
import random

import os



def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)


clearConsole()

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6

print(logo)
print(
    "Welcom to hangman game!!\n You are going to guess all of letters of a word.\n The word will be chosen randomly.\n What you need is to type a letter!!")

display = []
for _ in range(word_length):
    display += "_"

input_list = []

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    clearConsole()

    if len(guess) >= 2:
        guess = termcolor.colored(guess, "green")
        print("You typed", guess)
        print("Please type \"A\" letter")
        continue

    if guess == "":
        print("Please type a letter")

    elif guess in input_list:
        colored_guess = termcolor.colored(guess, "red")
        print(colored_guess, "has already guessed")
        print("You have already guessed these letters below")
        print(input_list)
        continue

    else:
        input_list.append(guess)

    for position in range(word_length):
        letter = chosen_word[position]

        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(guess, "is not in the word")
        print("you lose a life")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
            colored_word = termcolor.colored(chosen_word, "green")
            print(f"The word was {colored_word}")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print(cong)
        print("You win.")

    print(stages[lives])

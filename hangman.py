import os

import words


# Clears the terminal and displays a blank screen
os.system("clear")

# Asks the player there name and stores it
print("What is your name?", end=" ")
username = input()

# Says hello to the player
print("Hello " + username, "\nWelcome to a game of Hangman!")

# Gets a random word and calculates the length of the random word
word_to_guess = words.select_random_word()
length_of_word_to_guess = len(word_to_guess)

# Sets the current game state as a string of _, the amount of underscores is the length of the random word.
current_guess_state = list("_" * length_of_word_to_guess)

print("The word is", length_of_word_to_guess, "characters long.")
print("The current state is", words.print_current_state(current_guess_state))

print("Guess a letter.", end=" ")
guess = input()

current_guess_state, turn_result = words.player_guess(word_to_guess, guess, current_guess_state)
words.update_player(current_guess_state, turn_result)

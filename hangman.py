import os

import words


# Game variables
amount_of_lives = 10

# Asks the player there name and stores it, then says hello to them.
username = input("What is your name? ")
print("Hello " + username, "\nWelcome to a game of Hangman!")

# Gets a random word and calculates the length of the random word
word_to_guess = words.select_random_word()
length_of_word_to_guess = len(word_to_guess)
# Sets the current game state as a string of _, the amount of underscores is the length of the random word.
current_guess_state = list("_" * length_of_word_to_guess)

# While loop for while a game is running
game_loop = True
while game_loop:
    print(word_to_guess)
    words.print_current_game_state(length_of_word_to_guess, current_guess_state)

    # Gets input from the player
    user_guess = input("Guess a letter.")

    # Checks the players guess and returns an updated game state
    current_guess_state, turn_result = words.check_players_guess(word_to_guess, user_guess, current_guess_state)

    if turn_result:
        print("You were correct!")
    else:
        print("You were incorrect! You lose a life!")
        amount_of_lives -= 1

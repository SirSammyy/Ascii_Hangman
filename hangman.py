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

# List to hold the users guesses
players_guesses = []
# While loop for while a game is running
game_loop = True
while game_loop:
    print(word_to_guess)
    words.print_current_game_state(length_of_word_to_guess, current_guess_state)

    # Gets input from the player
    players_guess = input("Guess a letter. ")
    # Checks the players guess
    current_guess_state, turn_result = words.check_players_guess(word_to_guess, players_guess, current_guess_state, players_guesses)
    # Appends the guess to the list of already chosen guesses.
    players_guesses.append(players_guess)

    # Checks the result of the turn
    if turn_result == "Correct":
        print("You were correct!")
    elif turn_result == "Repeat":
        print("You used the letter '", players_guess, "' already.")
    elif turn_result == "Wrong":
        print("You were incorrect! You lose a life!")
        amount_of_lives -= 1
        # Checks if the user has any lives left
        if amount_of_lives <= 0:
            print("You have run out of lives.")
            print("Game Over")
            game_loop = False

    # Checks if the the entire word is correctly guessed
    if "".join(current_guess_state) == word_to_guess:
        print("You have Won!")
        game_loop = False

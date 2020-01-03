import os

import words


# Game variables
amount_of_lives = 10

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

# Prints out the current game state
words.print_current_game_state(length_of_word_to_guess, current_guess_state)

# Allows the user to guess a letter and returns the letter
user_guess = words.players_guess()

# Checks the players guess and returns an updated game state
current_guess_state = words.check_players_guess(word_to_guess, user_guess, current_guess_state)

game_loop = True
while game_loop:
    print(word_to_guess)
    words.print_current_game_state(length_of_word_to_guess, current_guess_state)
    user_guess = words.players_guess()
    # Checks the players guess and returns an updated game state
    current_guess_state, turn_result = words.check_players_guess(word_to_guess, user_guess, current_guess_state)

    if turn_result:
        print("You were correct!")
    else:
        print("You were incorrect! You lose a life!")
        amount_of_lives -= 1
        if amount_of_lives <= 0:
            print("Game Over! :()")
    if "".join(current_guess_state) == word_to_guess:
        game_loop = False
        words.print_current_guess_state(current_guess_state)
        print("You Win!")

import os

import hangman

# Asks the player there name and stores it, then says hello to them.
username = input("What is your name? ")
print("Hello " + username, "\nWelcome to a game of Hangman!")

program_loop = True
while program_loop:
    # Plays Hangman
    hangman.play_hangman()

    # Asks if the player wants to play again, and ends the loop if they don't
    play_again = input("Would you like to play again? (y or n): ")

    if play_again.lower() != "y":
        program_loop = False

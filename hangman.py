import random

from colours import Colours


list_of_words = ["Computer",
                 "Telephone",
                 "Laptop",
                 "Python",
                 "JavaScript",
                 "Monitor",
                 "Gloucester",
                 "Turnip",
                 "Carrot"]


def select_random_word():
    """
        Returns a random word from a pre-defined list
    """
    return random.choice(list_of_words)


def check_players_guess(word_to_guess, guess, current_guess_state, players_guesses):
    """

    """
    turn_result = "Wrong"

    if is_input_invalid(guess):
        turn_result = "Invalid"
    elif guess in players_guesses:
        turn_result = "Repeat"
    else:
        for idx, x in enumerate(word_to_guess):
            if guess == x or guess == x.swapcase():
                current_guess_state[idx] = x
                turn_result = "Correct"

    return current_guess_state, turn_result


def print_current_game_state(length_of_word_to_guess, current_guess_state, amount_of_lives, previous_guess):
    """

    """
    print("You have", amount_of_lives, "lives left.")
    print("The word is", length_of_word_to_guess, "characters long.")
    if previous_guess is not None:
        print("Your previous guess was", previous_guess)
    print("The current game state is:")
    print_current_guess_state(current_guess_state)
    return


def print_current_guess_state(current_guess_state):
    """

    """
    print(" ".join(current_guess_state))
    return


def is_input_invalid(user_input):
    if len(user_input) > 1:
        return True
    elif not user_input.isalpha():
        return True


def play_hangman():
    # Game variables
    amount_of_lives = 10

    # Gets a random word and calculates the length of the random word
    word_to_guess = select_random_word()
    length_of_word_to_guess = len(word_to_guess)
    # Sets the current game state as a string of _, the amount of underscores is the length of the random word.
    current_guess_state = list("_" * length_of_word_to_guess)

    # Holds the players guess and every guess so far.
    players_guess = None
    players_guesses = []

    # While loop for while a game is running
    game_loop = True
    while game_loop:
        print_current_game_state(length_of_word_to_guess, current_guess_state, amount_of_lives, players_guess)

        # Gets input from the player
        players_guess = input("Guess a letter. ")
        # Checks the players guess
        current_guess_state, turn_result = check_players_guess(word_to_guess, players_guess, current_guess_state, players_guesses)
        # Appends the guess to the list of already chosen guesses.
        players_guesses.append(players_guess)

        # Checks the result of the turn
        if turn_result == "Correct":
            print("You were correct!")
        elif turn_result == "Repeat":
            print("You used the letter '", players_guess, "' already.")
        elif turn_result == "Invalid":
            print("You entered an invalid guess, you must only input a single character which must be a letter.")
        elif turn_result == "Wrong":
            print(Colours.red + "You were incorrect! You lose a life!" + Colours.reset)
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

        # Prints a line of #, makes terminal output look better.
        print("###########################")

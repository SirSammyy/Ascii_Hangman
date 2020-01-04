import random

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

    if guess in players_guesses:
        turn_result = "Repeat"
    else:
        for idx, x in enumerate(word_to_guess):
            if guess == x or guess == x.swapcase():
                current_guess_state[idx] = x
                turn_result = "Correct"

    return current_guess_state, turn_result


def print_current_game_state(length_of_word_to_guess, current_guess_state, previous_guess=None):
    """

    """
    print("The word is", length_of_word_to_guess, "characters long.")
    print("The current game state is:")
    print_current_guess_state(current_guess_state)
    return


def print_current_guess_state(current_guess_state):
    """

    """
    print(" ".join(current_guess_state))
    return

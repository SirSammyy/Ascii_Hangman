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


def player_guess(word_to_guess, guess, current_guess_state):
    """

    """
    turn_result = False
    for idx, x in enumerate(word_to_guess):
        if guess == x or guess == x.swapcase():
            current_guess_state[idx] = x
            turn_result = True

    return current_guess_state, turn_result


def update_player(current_guess_state, turn_result):
    """

    """
    if turn_result:
        print("You were correct! The new state is:")
        print_current_state(current_guess_state)
    else:
        print("You were incorrect!")
    return


def print_current_state(current_guess_state):
    print(" ".join(current_guess_state))
    return

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

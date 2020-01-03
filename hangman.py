import words

print("What is your name?")

username = input()

print("Hello " + username, "\nWelcome to a game of Hangman!")

word_to_guess = words.select_random_word()

print("The word is", len(word_to_guess), "characters long.")

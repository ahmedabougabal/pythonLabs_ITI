"""
Word guessing game (hangman):
A list of words will be hardcoded in your program,
steps:
	- pick 1 random word
	- ask the user for his name
	- show the word with empty spots
	- continually ask the user to guess any alphabetical letter / or the word:
		if the word is correct:
			terminate the program and congratulate the player on winning
		elif the random word contains that letter:
			show all occurences of the letter in the correct spot (as well as previously correct guessed letters)
		else:
			let the user know he was wrong, and show the previous iteration of the correct guess letters
	- give the user maximum of 7 guess to complete the word


example:
please enter your name: "Abdallah"
the word that was picked is:  _ _ _ _ _ _ _
guess a letter: "a"
nice! that was in the word: _ a _ _ _ a _
guess a letter: "n"
nice! that was in the word: _ a n _ _ a n
guess a letter: "e"
no, that isn't in the word: _ a n _ _ a n
guess a letter: "h":
nice! that was in the word: h a n _ _ a n
guess a letter: "hangman"
the word is correct! congratulations


"""

import random

print("Welcome to the Hangman game!")
words = ["hangman", "lifting", "shooting", "madman", "electrocutioner"]
chosen = random.choice(words)
print(chosen)
guesses = 7
tries = 0
blanks = ["_" for _ in range(len(chosen))]

while tries < 7:
    user = input("Guess a letter or a word: ")
    if user.isdigit():
        print("Letters only accepted!")
        print("Try again")
        continue

    if user == chosen:
        print("Congrats! You guessed the correct word!")
        break

    if len(user) == 1:
        if user in chosen:
            for i, letter in enumerate(chosen):
                if letter == user:
                    blanks[i] = user
            print("Correct guess")
            print(" ".join(blanks))
            if "_" not in blanks:
                print("You have guessed it all right!")
                break
        else:
            print("Wrong guess")
            tries += 1
            guesses -= 1
            print(f"You have {guesses} guesses left.")
    else:
        print("Wrong guess")
        tries += 1
        guesses -= 1
        print(f"You have {guesses} guesses left.")

    if tries >= 7:
        print("You ran out of guesses")
        print("Game over!")
        break
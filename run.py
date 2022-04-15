import random
''' gives you access to the random module,
needed to choose a random word from wordList.py '''
from wordList import words
import string  # imports the string module


def getWord(words):
    word = random.choice(words)  # randomly chooses a word from the words list
    return word.upper()
# returns the word in uppercase to improve readability and consistency


def hangmanGame():
    word = getWord(words)  # gets a random word from the words list
    wordLetters = set(word)  # creates a set of the letters in the word
    alphabet = set(string.ascii_uppercase)
    ''' creates a set of the
    letters in the alphabet'''
    usedLetters = set()  # creates a set of the letters already used
    lives = 7

    while len(wordLetters) > 0 and lives > 0:
        print("\n")  # prints a new line
        print("Lives Remaining: " + str(lives))
        userLetter = input("\nGuess a letter: ").upper()
        if userLetter in alphabet - usedLetters:
            usedLetters.add(userLetter)  # adds the letter to the used letters set
        if userLetter in usedLetters:
            print("\nYou have already guessed that letter! Guess a different one.") 
        elif userLetter in wordLetters:
            wordLetters.remove(userLetter)
            print("\nNice Guess!")
        else:
            lives -= 1
            print("\nAhh, you lost a life. Try again!")
        if lives == 0:  # marks the end of the game
            print(hangmanLivesVisual[lives])  # prints the hangman lives visual
            print("Game over. You're dead. The word was: " + word)
            print("You win! The word was: " + word)

if __name__ == "__main__":
    hangmanGame()

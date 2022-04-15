import random
''' gives you access to the random module,
needed to choose a random word from wordList.py '''
from wordList import words
import string  # imports the string module

print(wordList)


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
 ''' sets the number of lives to 7 
  (includes the head, the body, the left arm, 
  the right arm, the left leg, and the right leg) '''
  
  while len(wordLetters) > 0 and lives > 0:  # while the word has letters and the user still has lives
    print("\n")  # prints a new line
    print("Lives Remaining: " + str(lives))  # prints the number of lives remaining
    
        userLetter = input("\nGuess a letter: ").upper() #asks the user to enter a letter (returns in uppercase)   
    if userLetter in alphabet - usedLetters:
      usedLetters.add(userLetter)  # adds the letter to the used letters set
    if userLetter in wordLetters:
        wordLetters.remove(userLetter)  # removes the letter from the word letters set
        print("\nNice Guess!")
            else:
        lives -= 1  # subtracts a life for incorrect guess
        print("\nAhh, you lost a life. Try again!")
            elif userLetter in usedLetters:
      print("\nYou have already guessed that letter! Guess a different one.")  
      # tells the user they have already guessed that letter
    else:
      print("\nThat is not a letter! Guess a different one.")  
      # prints an error message if the user enters a letter that is not in the alphabet
      
       if lives == 0:  # marks the end of the game
    print(hangmanLivesVisual[lives])  # prints the hangman lives visual
    print("Game over. You're dead. The word was: " + word)  # prints the word that the user was trying to guess
  else:
    print("You win! The word was: " + word)  # prints the word that the user guessed correctly
    
if __name__ == "__main__":
  hangmanGame()

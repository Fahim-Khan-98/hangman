

import random
import string
from word import words


#hangman
#Computer picks a word from a list
#player makes a guess one letter
#at a time


HANGMAN = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


WORDS = words







MAX_WRONG = len(HANGMAN) -1

#Initialize Variable

#Pick a word
word = random.choice(WORDS)



#Dashes for each letter
current_guess = len(word) * '-'


#Wrong Guess Counter
wrong_guess = 0

# Used letters Tracker
used_letter = []

# Main Loop
print("Welcome To HangMan")
print("Try to Guess the letters")

while wrong_guess < MAX_WRONG and current_guess != word:
    print(HANGMAN[wrong_guess])
    print("You have used the following letters: ",used_letter)
    print("So far the word is: ",current_guess)
    print(word)

    guess = input("Enter your letter guess: ")
    guess = guess.lower()


    #Check the letter was already used

    while guess in used_letter:
        print("You already guessed that letter",guess)
        guess = input("Enter your letter guess:")
        guess = guess.lower()
    
    #Add new guessed letter to list of guessed letters
    used_letter.append(guess)

    #Check guessed
    if guess in word:
        print("You have guessed correctly....")

        #Give a new version of the word with mixed letters and dashes
        new_current_guess = ""
        for letter in range(len(word)):
            if guess in word[letter]:
                new_current_guess += guess
            else:
                new_current_guess += current_guess[letter]

        current_guess = new_current_guess

    else:
        print("Sorry this was incorrect!!")
        wrong_guess +=1

#End the game

if wrong_guess == MAX_WRONG:
    print(HANGMAN[wrong_guess])
    print("You have been Hanged")
    print("Correct answer is : ",word)


else:
    print("You have won")



#!/usr/bin/env python3

import os
import time
import random
import banner

DICTIONARY = "./1000.txt"
MIN_WORD_LEN = 4
LIVES = 7
MASK = "_"


def intro():
    for n in range(1, 8):
        os.system("clear")
        time.sleep(1 / (2 * n))
        print(banner.BANNER)
        time.sleep(1 / (2 * n))
    os.system("clear")


def loadDict(DICTIONARY):
    with open(DICTIONARY, "r") as fopen:
        words = fopen.read().split("\n")
    return words


def randomWord(words):
    word = ""
    while len(word) < MIN_WORD_LEN:
        word = words.pop(random.randint(1, len(words)))
    return word


def newGame():
    word = randomWord(words)
    hg = Hangman(word, LIVES, MASK)
    return hg


class Hangman:
    def __init__(self, word, LIVES, MASK):
        self.word = word
        self.lives = LIVES
        self.mask = MASK
        # this will be displayed to the player
        self.secret = self.maskWord()
        # this list keep track of the wrong guesses
        self.usedLetters = []
        # turn word into a set to get the number of unique letters
        self.remainingLetters = len(set(self.word))
        # flag to indicate the end of the game
        self.over = False

    def __str__(self):
        """Create a printable version of the
        courrent state of the game"""
        mystring = str("""Lives left: {}\nUsed letters: {}\nWord: {}
        """.format(
                self.lives, ",".join(self.usedLetters), " ".join(self.secret)
            )
        )
        return mystring

    def maskWord(self):
        """Mask the letters in the word at game"""
        masked = list(self.word)
        for n in range(len(masked)):
            if masked[n].isalpha():
                masked[n] = self.mask
        return masked

    def validate(self, letter):
        """Check if the input letter is valid
        Update the secret, remaning letters and internal counters"""
        # a valid letter is in word and has not been used
        if letter in self.word and letter not in self.usedLetters:
            self.updateSecret(letter)
            self.usedLetters.append(letter)
            self.remainingLetters -= 1
            # when there are zero remaining letters the player has won
            if self.remainingLetters == 0:
                self.gameOver(True)
        # if a letter has been used we don't punish the player
        elif letter in self.usedLetters:
            print("The letter '{}' has already been used, try again!".format(letter))
        # if the letter is not valid we decrease the lives counter
        # and update the used letters list
        # if lives = 0 the player has lost
        else:
            self.lives -= 1
            self.usedLetters.append(letter)
            if self.lives == 0:
                self.gameOver(False)

    def updateSecret(self, letter):
        for n in range(len(self.word)):
            if letter == self.word[n]:
                self.secret[n] = letter

    def gameOver(self, value):
        if value:
            os.system("clear")
            print(self)
            print("The word was: '{}'".format(self.word))
            print("Congratulations, you guessed it!")
            # set lives to 0 to exit the loop
            self.over = True
        else:
            print("The word was: '{}', better luck next time!".format(self.word))
            self.over = True


#  display the cool intro
# intro()

# prepare the dictionary
words = loadDict(DICTIONARY)

player = input("Enter player's name and press Return\n")
print("Hi {}, let's play a game of hangman".format(player))

# repl
while True:
    hg = newGame()
    while not hg.over:
        os.system("clear")
        print(hg)
        letter = input("Guess a letter: ")
        hg.validate(letter)
    print("Good game {}, would you like to play again?".format(player))
    choice = input("Enter y or n and hit Return: ")
    if choice == "y":
        continue
    else:
        print("Ok, bye {}!".format(player))
        break

# todo
# add repl to allow multiple games
# filter multicharacter input
# fix the game logic when repeating the same letter
# add support for hyphens
# select dificulty (whole dictionary or most common words)
# print the complete word when the user guess the final letter

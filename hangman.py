import os
import time
import random

BANNER = """
                                                                                                                                         
                                                                                                                                         
HHHHHHHHH     HHHHHHHHH                                                                                                                  
H:::::::H     H:::::::H                                                                                                                  
H:::::::H     H:::::::H                                                                                                                  
HH::::::H     H::::::HH                                                                                                                  
  H:::::H     H:::::H    aaaaaaaaaaaaa  nnnn  nnnnnnnn       ggggggggg   ggggg   mmmmmmm    mmmmmmm     aaaaaaaaaaaaa  nnnn  nnnnnnnn    
  H:::::H     H:::::H    a::::::::::::a n:::nn::::::::nn    g:::::::::ggg::::g mm:::::::m  m:::::::mm   a::::::::::::a n:::nn::::::::nn  
  H::::::HHHHH::::::H    aaaaaaaaa:::::an::::::::::::::nn  g:::::::::::::::::gm::::::::::mm::::::::::m  aaaaaaaaa:::::an::::::::::::::nn 
  H:::::::::::::::::H             a::::ann:::::::::::::::ng::::::ggggg::::::ggm::::::::::::::::::::::m           a::::ann:::::::::::::::n
  H:::::::::::::::::H      aaaaaaa:::::a  n:::::nnnn:::::ng:::::g     g:::::g m:::::mmm::::::mmm:::::m    aaaaaaa:::::a  n:::::nnnn:::::n
  H::::::HHHHH::::::H    aa::::::::::::a  n::::n    n::::ng:::::g     g:::::g m::::m   m::::m   m::::m  aa::::::::::::a  n::::n    n::::n
  H:::::H     H:::::H   a::::aaaa::::::a  n::::n    n::::ng:::::g     g:::::g m::::m   m::::m   m::::m a::::aaaa::::::a  n::::n    n::::n
  H:::::H     H:::::H  a::::a    a:::::a  n::::n    n::::ng::::::g    g:::::g m::::m   m::::m   m::::ma::::a    a:::::a  n::::n    n::::n
HH::::::H     H::::::HHa::::a    a:::::a  n::::n    n::::ng:::::::ggggg:::::g m::::m   m::::m   m::::ma::::a    a:::::a  n::::n    n::::n
H:::::::H     H:::::::Ha:::::aaaa::::::a  n::::n    n::::n g::::::::::::::::g m::::m   m::::m   m::::ma:::::aaaa::::::a  n::::n    n::::n
H:::::::H     H:::::::H a::::::::::aa:::a n::::n    n::::n  gg::::::::::::::g m::::m   m::::m   m::::m a::::::::::aa:::a n::::n    n::::n
HHHHHHHHH     HHHHHHHHH  aaaaaaaaaa  aaaa nnnnnn    nnnnnn    gggggggg::::::g mmmmmm   mmmmmm   mmmmmm  aaaaaaaaaa  aaaa nnnnnn    nnnnnn
                                                                      g:::::g                                                            
                                                          gggggg      g:::::g                                                            
                                                          g:::::gg   gg:::::g                                                            
                                                           g::::::ggg:::::::g                                                            
                                                            gg:::::::::::::g                                                             
                                                              ggg::::::ggg                                                               
                                                                 gggggg                                                      Version 0.1a                                                         
"""

MIN_WORD_LEN = 4
LIVES = 7
DICTIONARY = "./1000.txt"
MASK = "_"


def intro():
    for n in range(1, 8):
        os.system("clear")
        time.sleep(1 / (2 * n))
        print(BANNER)
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
        mystring = str(
            """
        Lives left: {}
        Wrong guesses: {}
        Word: {}
        """.format(
                self.lives, self.usedLetters, ' '.join(self.secret)
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
            print("The word was: '{}'".format(self.word))
            print("Congratulations, you won!")
            # set lives to 0 to exit the loop
            self.over = True
        else:
            print("The word was: '{}', better luck next time!".format(self.word))
            self.over = True


words = loadDict(DICTIONARY)
word = randomWord(words)

hg = Hangman(word, LIVES, MASK)

while not hg.over:
    os.system('clear')
    print(hg)
    letter = input("Guess a letter: ")
    hg.validate(letter)


# todo
# finish when lives = 0
# check for already entered guesses
# print word if game ends
# select dificulty (whole dictionary or most common words)

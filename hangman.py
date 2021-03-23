import os
import time
import random

BANNER = '''
                                                                                                                                         
                                                                                                                                         
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
                                                                 gggggg                                                                  
'''

MIN_WORD_LEN = 4
LIVES = 7
DICTIONARY = './1000.txt'
MASK = '*'

def intro():
    for n in range(1,8):
        os.system("clear")
        time.sleep(1/(2*n))
        print(BANNER)
        time.sleep(1/(2*n))
    os.system("clear")


def loadDict(DICTIONARY):
    with open(DICTIONARY, 'r') as fopen:
        words = fopen.read().split('\n')
    return words

def randomWord(words):
    word = ''
    while len(word) < MIN_WORD_LEN: 
        word = words.pop(random.randint(1,len(words)))
    return word

class Hangman:
    def __init__(self, word, LIVES, MASK):
        self.word = word
        self.lives = LIVES
        self.mask = MASK
        self.secret = self.maskWord()
        self.used = ''
        self.finished = False
    
    def __str__(self):
        mystring = str('''
        Lives left: {}
        Wrong guesses: {}
        Word: {}
        '''.format(self.lives, self.used, self.secret))
        return mystring

    def maskWord(self):
        masked = list(self.word)
        for n in range(len(masked)):
            if masked[n].isalpha():
                masked[n] = self.mask
        return masked

    def validate(self, letter):
        for n in range(len(self.word)):
            if letter == self.word[n]:
                self.secret[n] = letter


words = loadDict(DICTIONARY)
word = randomWord(words)   

hg = Hangman(word, LIVES, MASK)

while not hg.finished:
    print(hg)
    letter = input('Guess a letter: ')
    hg.validate(letter)
    

# keep track of number of guesses and lives remaining
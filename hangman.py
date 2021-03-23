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
DICTIONARY = '../dictionaries/wordlist.txt'
MASK = '_'

def intro():
    for n in range(1,8):
        os.system("clear")
        time.sleep(1/(2*n))
        print(BANNER)
        time.sleep(1/(2*n))
    os.system("clear")


def loadDict():
    with open(DICTIONARY, 'r') as fopen:
        words = fopen.read().split('\n')
    return words

def randomWord():
    words = loadDict()
    word = words.pop(random.randint(1,len(words)))
    if len(word) > MIN_WORD_LEN:
        return word
    else:
        randomWord()



# hangman object
# choose a random word when created
# display underscores for each letter
# ask for input
# keep track of number of guesses and lives remaining
# reveal correct guesses
from colorama import Back, Fore 
import random

def print_green(letter):
    print(Back.GREEN + f" {letter} " + Back.RESET, end='')

def print_yellow(letter):
    print(Back.YELLOW + Fore.BLACK + f" {letter} " + Fore.RESET + Back.RESET, end='')

def print_gray(letter):
    print(Back.LIGHTBLACK_EX + f" {letter} " + Back.RESET, end='')



def read_wordlist(filename):

  words = []
  with open(filename, 'r') as f: 
    for line in f:
      words.append(line.strip())
  return words

WORDLIST_FILE = "wordle.txt"


def user_guess():   
  word = ''
  while len(word) != 5 and not word.isalpha():
    word = input("Please type a 5-letter word (letters only):")
    word = word.lower()
  return word


# The following is my initial implementation. Somethign like this 
# would have been fine for full credit. 


def print_word(word, guess):
  for i in range(len(guess)): 
    if word[i] == guess[i]: 
      print_green(guess[i])
    elif guess[i] in word: 
      print_yellow(guess[i])
    else: 
      print_gray(guess[i])
  print()


# However, one of you noticed that there is a corner case to
# consider
# https://edstem.org/us/courses/74694/discussion/6123241
#
# If the correct word contains a letter only once, but the 
# user guesses that letter twice -— once in the correct position 
# (green) and one in the wrong position -- should the 
# incorrectly placed occurrence still be marked yellow, even
# though the letter has already been accounted for in the correct 
# position? Ideally, we would want the second occurence to show
# as incorrect (gray).
from collections import defaultdict
def print_word(word, guess):

  letter_count = defaultdict(int)
  correct = set()
  for letter in word:
    letter_count[letter] += 1 

  for i in range(len(guess)):     
    if word[i] == guess[i]:
      correct.add(i)
      letter_count[word[i]] -= 1

  for i in range(len(guess)): 
    if i in correct:
      print_green(guess[i])
    elif letter_count[guess[i]] > 0:  
      print_yellow(guess[i])
      letter_count[guess[i]] -= 1
    else: 
      print_gray(guess[i])
  print()



def wordle():

  wordlist = read_wordlist(WORDLIST_FILE)

  word = random.choice(wordlist)

  guesses = 1

  while guesses <= 6:

    guess = user_guess()
    
    if guess in wordlist: 

      print_word(word, guess)

      print(f"Guesses: {guesses}/6")

      if guess == word: 
        print("Congratulations!")
        return
      
      else: 
        guesses += 1
    else: 
      print("Not in wordlist")

  print(f"Out of guesses. Maybe next time! The word was {word}")
  

if __name__ == "__main__":
  wordle()

import os
from random import choice
os.system("cls")

'''Start of Global variables'''
#gameon = True
letterpositions = []
incorrectguesses = []
#art adapted from http://ascii.co.uk/art/hangman
hangman = [
r'''
 ___________.._______
| .__________________|
| | / /
| |/ /
| | /
| |/
| |
| |
| |
| |
| |
| |
| |
| |
| |
| |
| |
| |
""""""""""""""""""""|"""|
|"|"""""""""""""""""'"|"|
| |                   | |
: :                   : :
. .                   . .
''',
r'''
 ___________.._______
| .__________________|
| | / /
| |/ /
| | /
| |/
| |
| |
| |
| |
| |
| |
| |
| |          ||
| |          ||
| |          ||
| |          ||
| |         / |
""""""""""""""""""""|"""|
|"|"""""""""""""""""'"|"|
| |                   | |
: :                   : :
. .                   . .
''',
r'''
 ___________.._______
| .__________________|
| | / /
| |/ /
| | /
| |/
| |
| |
| |
| |
| |
| |
| |
| |          ||'||
| |          || ||
| |          || ||
| |          || ||
| |         / | | \
""""""""""""""""""""|"""|
|"|"""""""""""""""""'"|"|
| |                   | |
: :                   : :
. .                   . .
''',
r'''
 ___________.._______
| .__________________|
| | / /
| |/ /
| | /
| |/
| |
| |
| |         .-`--'.
| |         Y . . Y
| |          |   |
| |          | . |
| |          |   |
| |          ||'||
| |          || ||
| |          || ||
| |          || ||
| |         / | | \
""""""""""""""""""""|"""|
|"|"""""""""""""""""'"|"|
| |                   | |
: :                   : :
. .                   . .
''',
r'''
 ___________.._______
| .__________________|
| | / /
| |/ /
| | /
| |/
| |
| |
| |         .-`--'.
| |        /Y . . Y
| |       // |   |
| |      //  | . |
| |     ')   |   |
| |          ||'||
| |          || ||
| |          || ||
| |          || ||
| |         / | | \
""""""""""""""""""""|"""|
|"|"""""""""""""""""'"|"|
| |                   | |
: :                   : :
. .                   . .
''',
r'''
 ___________.._______
| .__________________|
| | / /
| |/ /
| | /
| |/
| |
| |
| |         .-`--'.
| |        /Y . . Y\
| |       // |   | \\
| |      //  | . |  \\
| |     ')   |   |   (`
| |          ||'||
| |          || ||
| |          || ||
| |          || ||
| |         / | | \
""""""""""""""""""""|"""|
|"|"""""""""""""""""'"|"|
| |                   | |
: :                   : :
. .                   . .
''',
r'''
 ___________.._______
| .__________________|
| | / /
| |/ /
| | /          .-''.
| |/          /  _  \
| |           |  `/,|
| |           | `_.'
| |         .-`--'.
| |        /Y . . Y\
| |       // |   | \\
| |      //  | . |  \\
| |     ')   |   |   (`
| |          ||'||
| |          || ||
| |          || ||
| |          || ||
| |         / | | \
""""""""""""""""""""|"""|
|"|"""""""""""""""""'"|"|
| |                   | |
: :                   : :
. .                   . .
''',
r'''
 ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \
| |          ||  `/,|
| |          (\\`_.'
| |         .-`--'.
| |        /Y . . Y\
| |       // |   | \\
| |      //  | . |  \\
| |     ')   |   |   (`
| |          ||'||
| |          || ||
| |          || ||
| |          || ||
| |         / | | \
""""""""""|_`-' `-' |"""|
|"|"""""""\ \       '"|"|
| |        \ \        | |
: :         \ \       : :
. .          `'       . .

'''
]



'''End of global variables'''

'''Start of function definitions'''

def print5lines():
  '''Print 5 blank lines'''
  print""
  print""
  print""
  print""
  print""

def print10lines():
  '''Print 10 blank lines'''
  print5lines()
  print5lines()

def guessindex(guess):
  '''Creates a list of index values where the guess appears'''
  index = 0
  letterpositions = []
  while index < len(solution):
    for letter in solution:
      if letter == guess:
        letterpositions.append(index)
      index += 1
  return letterpositions

def solve(guess, letterpositions):
  '''Rewrite the blanks list with the guess in place'''
  for index in letterpositions:
    blanks[index] = guess
  return blanks

def nextscreen(guess, incorrectguesses):
  '''Initiate the next play screen.'''
  os.system("cls")
  print10lines()
  guessindex(guess)
  letterpositions = guessindex(guess)
  print hangman[len(incorrectguesses)]
  print '[%s]' % ' '.join(map(str,solve(guess, letterpositions)))
  print "Incorrect Guesses: ", incorrectguesses

'''#Check if solution achieved
def isgameon(solution,solve):
  return solution != solve'''

#Acquire new guess from player
def getguess():
  guess = raw_input("Guess a letter. ")
  return guess


'''End of function definitions'''



#Welcome screen

print "Welcome to Hangman!"
print""
usescrabble = raw_input("Do you want to play from the scrabble dictionary? ")
print""

if usescrabble == "yes" or usescrabble == "Yes":
  WORD_LIST = "sowpods.txt"
  wordlist = file(WORD_LIST, 'r').readlines()
  # Get rid of newlines
  wordlist = [word.lower().strip() for word in wordlist]
  shortlist = []
  for word in wordlist:
    if len(word) > 8:
        shortlist.append(word)
  solution = list(choice(shortlist))
else:
    #User enters phrase for hangman
    rawsolution = raw_input("Enter a phrase for the hanged man. ")
    print""
    solution = list(rawsolution.lower())

#Create the blanks
blanks = []
for letter in solution:
  if letter == " ":
    display = " "
    blanks.append(display)
  else:
    display = "-"
    blanks.append(display)

#Initiate the first play screen
os.system("cls")
print hangman[0]
print '[%s]' % ' '.join(map(str,blanks))
print""
guess = getguess()

#Add incorrect guesses to a list
if guess not in solution:
  incorrectguesses.append(guess)

#Display guess results and get new guess
while solution != solve(guess, letterpositions):
  nextscreen(guess, incorrectguesses)
  if len(incorrectguesses) == len(hangman)-1:
    print "You have lost."
    print ""
    print "The answers was", '[%s]' % ' '.join(map(str,solution))
    print ""
    break
  if solution != solve(guess, letterpositions):
    guess = getguess()
    if guess not in solution:
      incorrectguesses.append(guess)
else:
  print "Congratulations! You've got it!"



'''
solve = []

index = 0
if guess in solution:
  while index < len(solution)-1:
    if guess == solution[index]:
      solve.append(guess)
      index += 1
    else:
      solve.append("-")
      index += 1


print solve
'''






from os import system
from random import choice
from art import hangman

system("cls")

'''Start of Global variables'''
#gameon = True
letterpositions = []
incorrectguesses = []
'''End of global variables'''

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
  system("cls")
  print hangman[len(incorrectguesses)]
  print '[%s]' % ' '.join(map(str,solve(guess, (guessindex(guess)))))
  print "Incorrect Guesses: %s" % ' '.join(map(str, incorrectguesses))

#Acquire new guess from player
def getguess():
  guess = raw_input("Guess a letter. ")
  return guess

def getscrabbleword():
    WORD_LIST = "sowpods.txt"
    wordlist = [word.lower().strip() for word in file(WORD_LIST, 'r').readlines()]
    shortlist = []
    for word in wordlist:
        if len(word) > 8:
            shortlist.append(word)
    solution = list(choice(shortlist))
    return solution

def welcomescreen():
    print "Welcome to Hangman!"
    print""
    usescrabble = raw_input("Do you want to play from the scrabble dictionary? ")
    print""
    if usescrabble == "yes" or usescrabble == "Yes":
        solution = getscrabbleword()
    else:
        #User enters phrase for hangman
        solution = list(raw_input("Enter a phrase for the hanged man. ").lower())
    return solution
    
def createtheblanks(solution):
    blanks = []
    for letter in solution:
      if letter == " ":
        blanks.append(" ")
      else:
        blanks.append("-")
    return blanks
    
def initiatestocks():
    system("cls")
    print hangman[0]
    print '[%s]' % ' '.join(map(str,blanks))
    print""
    
solution = welcomescreen()

blanks = createtheblanks(solution)

initiatestocks()

guess = getguess()

#Add incorrect guesses to a list
if guess not in solution:
  incorrectguesses.append(guess)

#Display guess results and get new guess
while solution != solve(guess, letterpositions):
  nextscreen(guess, incorrectguesses)
  if len(incorrectguesses) == len(hangman)-1:
    print "You have lost."
    #Eventually show a picture of the guy from Space Quest.
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







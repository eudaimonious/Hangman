from os import system
import string
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
  '''Rewrite the solvedsofar list with the guess in place'''
  for index in letterpositions:
    solvedsofar[index] = guess
  return solvedsofar

def nextscreen(guess, incorrectguesses):
  '''Initiate the next play screen.'''
  system("cls")
  print hangman[len(incorrectguesses)]
  print '[%s]' % ' '.join(map(str,solve(guess, (guessindex(guess)))))
  print "Incorrect Guesses: %s" % ' '.join(map(str, incorrectguesses))

#Acquire new guess from player
def getguess():
  guess = raw_input("Guess a letter. ")
  if validguesstest(guess) == "Fail":
    print "Let's try that again. Please guess a letter. "
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

def validphrasetest(userinput):
    validcharacters = string.letters + " "
    for i in userinput:
        if i not in validcharacters:
            result = "Fail"
            return result
        else:
            result = "Pass"
    return result
    
def validguesstest(userinput):
    validcharacters = string.letters
    if len(userinput) > 1:
        result = "Fail"
        return result
    elif userinput not in validcharacters:
        result = "Fail"
        return result
    else:
        result = "Pass"
    return result
    
       
            
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
        if validphrasetest(solution) == "Fail":
            print "Please try again, entering only letters and spaces."
            solution = list(raw_input("Enter a phrase for the hanged man. ").lower())
    return solution
    
def createsolvedsofar(solution):
    solvedsofar = []
    for letter in solution:
      if letter == " ":
        solvedsofar.append(" ")
      else:
        solvedsofar.append("-")
    return solvedsofar
    
def initiatestocks():
    system("cls")
    print hangman[0]
    print '[%s]' % ' '.join(map(str,solvedsofar))
    print""
    
solution = welcomescreen()

solvedsofar = createsolvedsofar(solution)

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







#A Simple number guessing game

#imort the libraries
import random
import sys

#function for genarate random numbers according to the levels
def level(lvl):
    global randNo
    if lvl == 'E':
        randNo = random.randint(1,10)
        print('Guess a number between 1 & 10..')

    elif lvl == 'N':
        randNo = random.randint(1,20)
        print('Guess a number between 1 & 20..')

    elif lvl == 'H':
        randNo = random.randint(1,30)
        print('Guess a number between 1 & 30..')

    else:
        sys.exit('Invalid Input')

    return randNo 

#function for take the guessed numbers
def guessNo(randNo):
    print('.......')
    print('You have only 3 chances')
    for i in range(0,3):
        global guess
        guess = int(input('Enter your guessed number : '))

        if guess < randNo :
            print('The number Is Too Low')
        elif guess > randNo:
            print('The number Is Too High')

        else:
           break

        
    

print('***************************')
print('     GUESS THE NUMBER       ')
print('***************************\n')
print('Select a level')
print('(Enter the level first letter)')
lvl = input('Easy\t- E\nNormal\t- N\nHard\t- H\n')
print('\nI am currently thinking a Number...')

randNo = level(lvl)
guessNo(randNo)

print('\n***************************')
#Checking the input number and random number
if guess == randNo:
    print('Congradulations! You guessed the number..')

else:
    print('Oops...Better Luck Next Time!')
    print('Correct number was '+str(randNo))

print('***************************')

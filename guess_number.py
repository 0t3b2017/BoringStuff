# This is a guess the number game.
import random

name = input('Hello. What is your name? ')

print('Well, ' + name + ', I am thinking of a number between 0 and 20.')
secretNumber = random.randint(1, 20)

for guessesTaken in range(1, 7):
    guess = int(input('Take a guess.'))

    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high')
    else:
        break  # This condition is for the correct guess!

if guess == secretNumber:
    print('Good job, ' + name + '! You guessed my number in ' + str(guessesTaken) + ' guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber) + '!')

#!/usr/bin/env python3

import random

time = 0
inputValue = 0
secretValue = random.randint(1, 20)

for guestTaken in range(7):
    print("Take a guest")
    inputValue = int(input())

    if inputValue < secretValue:
        print("You guess too low")
    elif inputValue > secretValue:
        print("You guess too high")
    else:
        break;

if inputValue == secretValue:
    print("Good job! You guessed my number in "+str(guessTaken) + " guesses!")
else:
    print("Nope, the number is " + str(secretValue))



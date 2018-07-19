#!/usr/bin/env python3

def collatz(Number):
    if Number%2 == 0:
        print(Number//2)
        return Number//2
    else:
        print(Number*3+1)
        return Number*3+1

if __name__ == '__main__':
    print("Please input a number:")
    try:
        NewNumber = int(input())
    except ValueError:
        print("You have to input an integeter number")
    else: 
        NewNumber = collatz(NewNumber)
        while NewNumber != 1:
            NewNumber = collatz(NewNumber)

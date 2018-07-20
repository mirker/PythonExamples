#!/usr/bin/env python

def IsPrime(number):
    x = number//2
    while x > 1:
        if number % x == 0:
            print number, ' has factor ', x
            break;
        x = x - 1
    else:
        print number, ' is prime'


for i in range(0, 100000):
    IsPrime(i)

IsPrime(15.0)
            

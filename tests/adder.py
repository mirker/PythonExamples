#!/usr/bin/env python

def adder(val1, val2):
    return val1 + val2

string1='This is '
string2='a test string'

list1=[1,2,3,4]
list2=[i for i in range(7, 12)]

float1=1.23
float2=0.199

print adder(string1, string2), adder(list1, list2), adder(float1, float2) 

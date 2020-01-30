#!/usr/bin/env python

import re

def PasswordValid(password):
    if len(password) < 8:
        return False
    captionReg = re.compile(r'\w*[A-Z]+\w*')
    lowReg = re.compile(r'\w*[a-z]+\w*')
    digitReg = re.compile(r'\w*\d+\w*')
    caption_result = captionReg.search(password)
    low_result = lowReg.search(password)
    digit_result = digitReg.search(password)

    return (caption_result != None) and (low_result != None) and (digit_result != None)

if __name__ == '__main__':
    while True:
        password = raw_input()
        if PasswordValid(password):
            break
        else:
            print "Please retry"
            

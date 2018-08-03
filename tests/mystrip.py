#!/usr/bin/env python3
import re

def myStrip(target, stripChar=None):
    if stripChar == None:
        Regex = re.compile(r'^(\s*)|(\s*)$')
        return Regex.sub(r'', target)
    else:
        Regex = re.compile(stripChar[0])
        return Regex.sub(r'', target)

if __name__ == '__main__':
    print(myStrip('    This a test  '))
    print(myStrip('    This a test  ', 't'))
    

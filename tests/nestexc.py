#!/usr/bin/env python

def action2():
    print 1+[]    #Generate TypeError

def action1():
    try:
        action2()
    except TypeError:
        print 'inner try'

if __name__ == '__main__':
    try:
        action1()
    except TypeError:
        print 'outside try'


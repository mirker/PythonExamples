#!/usr/bin/env python

class adder:
    def __init__(self, value=0):
        self.data = value
    def __add__(self, other):
        self.data += other

class addrepr(adder):
    def __repr__(self):
        return 'addrepr(%s)' % self.data

class addstr(adder):
    def __str__(self):
        return '[Value: %s]' % self.data

class addboth(adder):
    def __str__(self):
        return '[Value: %s]' % self.data
    def __repr__(self):
        return 'addboth(%s)' % self.data
    
if __name__ == '__main__':
    x = addrepr(2)
    x + 1
    print x
    print str(x), repr(x)

    y = addstr(3)
    y + 1
    print y
    print str(y), repr(y)

    z = addboth(4)
    z + 1
    print z
    print str(z), repr(z)

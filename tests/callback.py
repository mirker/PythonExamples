#!/usr/bin/env python

class Callback:
    def __init__(self, color):
        self.color = color
    def __call__(self):
        print 'turn ', self.color
    def changeColor(self):
        print 'turn ', self.color

if __name__ == '__main__':
    cb3 = (lambda color='red': 'turn ' + color)
    print cb3() 

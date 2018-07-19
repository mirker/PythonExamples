#!/usr/bin/env python

class life:
    def __init__(self, name='unknown'):
        print 'Hello', name
        self.name = name
    def __del__(self):
        print 'Goodbye', self.name

if __name__=='__main__':
    brian = life('Brian')
    brian = 'loretta'

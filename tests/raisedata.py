#!/usr/bin/env python

myException = 'Error'

def raise1():
    raise myException, "hello"

def raise2():
    raise myException

def tryer(func):
    try:
        func()
    except myException, extraInfo:
        print 'got this: ', extraInfo

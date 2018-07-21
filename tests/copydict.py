#!/usr/bin/env python
import copy

def copyDict(dict):
    newdict = {}
    for key in dict.keys():
        newdict[key] = dict[key]
    
    return newdict

print copyDict({'a':1, 'b':2})


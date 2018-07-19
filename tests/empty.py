#!/usr/bin/env python

class empty:
    def __getattr__(self, attrname):
        if attrname == "age":
            return 40
        else:
            raise AttributeError, attrname

class accesscontrol:
    def __setattr__(self, attr, value):
        if attr == "age":
            self.__dict__[attr] = value
        else:
            raise AttributeError, attr + ' not allowed'
        
if __name__ == "__main__":
    X = empty()
    Y = accesscontrol()
    print X.age
    Y.age = 41
    print Y.age
    #X.name
    Y.name = 'mel'

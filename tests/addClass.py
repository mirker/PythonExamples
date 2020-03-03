#!/usr/bin/env python


class Adder:
    def __init__(self, data):
        self.data = data
        
    def add(self, x, y):
        print("Not Implemented")


class ListAdder(Adder):
    def add(self, x, y):
        return x+y
    def __add__(self, y):
        return self.data + y

class DictAdder(Adder):
    def add(self, x, y):
        z = {}
        for k in x.keys():
            z[k] = x[k]
        for k in y.keys():
            z[k] = y[k]
        return z

    def __add__(self, y):
        return self.add(self.data, y)
        

if __name__ == '__main__':
    #print ListAdder().add([1, 2], [3, 4])
    #print DictAdder().add({'a': 1, 'b': 2}, {'b': 3, 'd': 4})
    print(ListAdder([1,2])+ [3,4])
    print(DictAdder({'a':1, 'b':2}) + {'c':4, 'a':3})

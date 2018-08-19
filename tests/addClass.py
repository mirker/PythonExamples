#!/usr/bin/env python


class Adder:
    def add(self, x, y):
        print "Not Implemented"


class ListAdder(Adder):
    def add(self, x, y):
        return x+y


class DictAddr(Adder):
    def add(self, x, y):
        z = {}
        for k in x.keys():
            z[k] = x[k]
        for k in y.keys():
            z[k] = y[k]
        return z


if __name__ == '__main__':
    print ListAdder().add([1, 2], [3, 4])
    print DictAddr().add({'a': 1, 'b': 2}, {'b': 3, 'd': 4})

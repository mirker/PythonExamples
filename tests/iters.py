#!/usr/bin/env python

class Squares:
    def __init__(self, start, stop):
        self.value = start - 1
        self.stop = stop

    def __iter__(self):
        return self

    def next(self):
        if self.value == self.stop:
            raise StopIteration
        self.value += 1
        return self.value**2

if __name__ == "__main__":
    for i in Squares(1, 5):
        print i,

    X = Squares(1, 5)
    print [n for n in X]
    print [n for n in X]

    print [n for n in Squares(1, 5)]
    print list(Squares(1, 3))

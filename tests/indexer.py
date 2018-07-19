#!/usr/bin/env python

class indexer:
    def __getitem__(self, index):
        return index**2

if __name__ == '__main__':
    X = indexer()

    print X[2]
    for i in range(5):
        print X[i],

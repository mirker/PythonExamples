#!/usr/bin/env python
L = [1, 2, 4, 8, 16, 32, 64]
X = 15

if 2 ** X in L:
    print 'at index', L.index(2 ** X)
else:
    print X, 'not found'

L2 = [2**i for i in range(7)]
print L2

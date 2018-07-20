#!/usr/bin/env python
import math

L = [2, 4, 9, 16, 25]

newL = []

for i in L:
    newL.append(math.sqrt(i))

print newL

newL2 = map(math.sqrt, L)
print newL2

newL3 = [math.sqrt(i) for i in L]
print newL3

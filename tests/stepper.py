#!/usr/bin/env python

class stepper:
    def __getitem__(self, i):
        return self.data[i]

if __name__ == "__main__":
    X = stepper()
    X.data = "Spam"
    print X[1]

    for item in X:
        print item

    print 'p' in X

    print [c for c in X]

    print map(None, X)

    (a, b, c, d) = X
    print a, b, c, d

    print list(X)
    print tuple(X)
    print ''.join(X)

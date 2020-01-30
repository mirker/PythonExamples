#!/usr/bin/env python

class FormatError:
    def __init__(self, line, file):
        self.line = line
        self.file = file

    def logerror(self):
        log = open('formaterror.txt', 'a')
        print >> log, 'Erro at', self.file, self.line

def parser():
    raise FormatError(40, 'spam.txt')

if __name__ == '__main__':
    try:
        parser()
    except FormatError, exc:
        exc.logerror()

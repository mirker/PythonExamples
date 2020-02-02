#!/usr/bin/env python
"""
Count a file's line number and char number
"""

import argparse

def countLines(fileId):
    lineNumber = len(fileId.readlines())
    return lineNumber

def countChars(fileId):
    fileId.seek(0)
    charNumber = len(fileId.read())
    return charNumber

def test(fileName):
    fd = open(fileName, 'r')
    print("%s has: %d lines and %d char" % (fileName, countLines(fd), countChars(fd)))
    fd.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='count file inofmration')
    parser.add_argument('--file', action='store', dest='filename')
    given_args = parser.parse_args()
    filename = given_args.filename
    test(filename)

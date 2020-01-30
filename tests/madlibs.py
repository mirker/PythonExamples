#!/usr/bin/env python3

import sys, shelve, re

ADJECTIVE_STR = "ADJECTIVE"
NOUN_STR = "NOUN"
VERB_STR = "VERB"

if len(sys.argv) == 2:
    with open(sys.argv[1], "r") as sourceFile, open('target_'+ sys.argv[1], "w") as targetFile:
            for line in sourceFile:
                bReplaced = True
                while bReplaced:
                    bReplaced = False
                    if ADJECTIVE_STR in line:
                        print("Enter ADJ: ")
                        Adj = input()
                        line = line.replace(ADJECTIVE_STR, Adj, 1)
                        print(line)
                        bReplaced = True
                        
                    if NOUN_STR in line:
                        print("Enter Noun: ")
                        Noun = input()
                        line = line.replace(NOUN_STR, Noun, 1)
                        print(line)
                        bReplaced = True
                        
                    if VERB_STR in line:
                        print("Enter Verb: ")
                        Verb = input()
                        line = line.replace(VERB_STR, Verb, 1)
                        print(line)
                        bReplaced = True

                print(line)
                targetFile.write(line)


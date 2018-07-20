#!/usr/bin/python
import string


dict = {"a": "123", "b":"456", "c":"789"}
#string = "abc"
print string.maketrans(dict)

dict = {97:"123", 98:"456", 99:"789"}
#string = "abc"
print string.maketrans(dict)

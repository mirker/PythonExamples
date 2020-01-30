#!/usr/bin/env python

def myAddr(a, b):
    return a+b

def myAddr1(*args):
    result = args[0]
    for elm in args[1:]:
        result += elm
    return result

def myAddr2(good = 1, bad = 2, ugly = 3):
    return good + bad + ugly

def myAddr3(**args):
    args = list(args.values())
    ret = args[0]
    for elm in args[1:]:
        ret += elm
    return ret

def myAddr4(**args):
    keys = list(args.keys())
    for elm in keys:
        print(type(elm))
    return 0

def copyDict(dict):
    newOne = {}
    for key in dict.keys():
        newOne[key] = dict[key]
    return newOne
	
def addDict(dict1, dict2):
	newOne = {}
	for key in list(dict1.keys()):
		newOne[key]=dict1[key]
	
	for key in list(dict2.keys()):
		newOne[key]=dict1[key]
	return newOne

if __name__ == '__main__':
    print(myAddr1(1, 2, 3, 4))
    print(myAddr1('a', 'b', 'efaaa', 'test'))
    print(myAddr1([1,2,3], ['ab', 'd', 'f']))
    #print(myAddr1(1, 'ab'))
    #print(myAddr1({1:'a'}, {2:'d'}))
    print(myAddr2())
    print(myAddr2(bad = 1))
    print(myAddr2(bad = 0, good = 0, ugly = 0))
    print(myAddr2(2))
    print(myAddr2(0,0))

    print(myAddr3(a=4, b=2, d=3))
    print('-----')
    print(myAddr4(a=3, b=2, c=1, d= 3))

    print(copyDict({'a':1,'b':2,'c':3}))

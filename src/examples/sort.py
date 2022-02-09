#!/usr/bin/env python


def sort(array):
    for i in range(len(array) - 1):
        for j in range(len(array) - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


if __name__ == '__main__':
    a = [56, 23, 233, 0, -1, 34]
    sort(a)
    print(a)

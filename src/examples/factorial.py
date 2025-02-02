#!/usr/bin/env python


def fac():
    num = int(input("请输入一个数字:"))
    factorial = 1
    # 查看数字是负数， 0 或者正数
    if num < 0:
        print("抱歉，负数没有阶乘")
    elif num == 0:
        print("0的阶乘为1")
    else:
        for i in range(1, num + 1):
            factorial = factorial * i
    print("%d 的阶乘为 %d" % (num, factorial))


def factorial(n):
    result = n
    for i in range(1, n):
        result *= i
    return result


def fact(n):
    if n == 1:
        return 1
    return n * fact( n - 1 )


if __name__ == '__main__':
    a = factorial(3)
    print(a)

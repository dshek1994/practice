#!/usr/bin/env python3

def Fibonacci(n):

    if n < 0:
        print("Incorrect")
    
    elif n == 0:
        return 0
    
    elif n == 1 or n == 2:
        return 1
    
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)


def isEven(num):

    for x in range(1, num):
        if Fibonacci(x)%2 == 0:
            print(Fibonacci(x))

isEven(20)


#!/usr/bin/env python3

def isPrime(n):

    #corner case
    if (n <= 2):
        return False
    
    #check from 2 to n-1
    for i in range(2, n):
        if (n % i == 0):
            return False

    return True

def largestPrimeFactor(num):

    largestFactor = 0

    for i in range(2, num):
        if (num % i == 0):
            if (isPrime(i) == True):
                if (i > largestFactor):
                    largestFactor = i
    
    print(largestFactor)

largestPrimeFactor(13195)
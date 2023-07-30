#!/usr/bin/env python3

def print_fibonacci(length):
    fib = []
    if(length == 0):
        print(fib)
    elif(length== 1):
        fib.append(0)
        print(fib)
    else: 
        fib.append(0)
        fib.append(1)
        newElement = 0
        for i in range(length-2):
            # print(f'i: {i}')
            newElement = fib[i] + fib[i+1]
            fib.append(newElement)
            # print(f'fib: {fib}')
    
        print(fib)
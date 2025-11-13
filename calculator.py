#https://github.com/NataliaVeltri/lab11-NV-IG/tree/main
#Partner 1: Natalia Veltri
#Partner 2: Izzie Gomez

import math
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
def square_root(a):
    if a < 0:
        raise ValueError
    return math.sqrt(a)


def hypotenuse(a, b):
    try:
        return math.hypot(a, b)
    except Exception as e:
        print(f"Error: {e}")


def add(a, b): 
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        raise ZeroDivisionError
    return a / b

def logarithm(a, b):
    if a <= 0:
        raise ValueError
    if b <= 0:
        raise ValueError
    if b == 1:
        if a == 1:
            raise ValueError
        return 0
    return math.log(a , b)

def exp(a,b):
    return a**b

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
    try:
        if a < 0:
            raise ValueError
        return math.sqrt(a)
    except ValueError as e:
        print(f"Error: {e}")


def hypotenuse(a, b):
    try:
        return math.hypot(a, b)
    except Exception as e:
        print(f"Error: {e}")


def add(a, b): 
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    return b / a

def log(a, b):
    import math
    if a <= 0 or b <= 0 or b == 1:
        raise ValueError
    return math.log(a, b)

def exp(a,b):
    return a**b

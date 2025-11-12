import math

def add(a, b): 
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError("You can't divide by 0")
    return b / a

def log(a, b):
    if a <= 0 or b <= 0 or a == 1:
        raise ValueError("This log function is not valid.")
    return math.log(b, a)

def exp(a, b):
    return a ** b






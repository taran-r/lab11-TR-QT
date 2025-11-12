# https://github.com/taran-r/lab11-TR-QT
# Partner: Taran Raj
# Partner: Quocnghia Truong
import math

import math
# First example
def add(a, b): 
    return a + b

def add(a, b): 
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b



def log(a, b):
    if a <= 0 or b <= 0 or a == 1:
        raise ValueError("This log function is not valid.")
    return math.log(b, a)

def exp(a, b):
    return a ** b





def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    return b / a

def log(a, b):
    if a <= 0 or a == 1:
        raise ValueError
    if b <= 0:
        raise ValueError
    return math.log(b) / math.log(a)

def exp(a, b):
    return a**b


# https://github.com/taran-r/lab11-TR-QT
# Partner: Taran Raj
# Partner: Quocnghia Truong
import math

def square_root(a):
    try:
        if a < 0:
            raise ValueError("You can't square root a negative number.")
        return math.sqrt(a)
    except TypeError:
        raise TypeError('The number must be a float or int')
    except Exception as e:
        print(f"The following error occured: {e}")
        raise

def hypotenuse(a, b):
    try:
        return math.hypot(a, b)
    except TypeError:
        raise TypeError("The numbers a and b must be a float or int")
    except Exception as e:
        print(f"The following error occured: {e}")
        raise

def add(a, b): 
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Can't divide by 0.")
    return b / a

def logarithm(a, b):
    if a <= 0 or b <= 0 or a == 1:
        raise ValueError("This log function is not valid.")
    return math.log(b, a)

def exp(a, b):
    return a ** b


# open test_calc.py for instructions on how to run the test


def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError('You cant divide by 0')
    else:
        return a / b

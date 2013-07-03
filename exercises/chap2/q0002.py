#!/usr/bin/python

def fizzbuff(n):
    """ Return 'FizzBuzz' String

    Arguments:
        n - some number

    Returns: string
        If it is a divisor of 3  - Fizz
        If it is a divisor of 5  - Buzz
        If it is a divisor of 15 - Fizz Buzz
    """
    if n % 15 == 0:
        return 'Fizz Buzz'
    elif n % 3 == 0:
        return 'Fizz'
    elif n % 5 == 0:
        return 'Buzz'
    return n

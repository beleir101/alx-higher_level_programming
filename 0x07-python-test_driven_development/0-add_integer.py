#!/usr/bin/python3
""" Module to demonstrate test using doctest"""


def add_integer(a, b=98):
    """ Adds two integers
        a and b must be integers or floats,
        otherwise raise a TypeError exception with the message
        a must be an integer
        or b must be an integer
        a and b must be first casted to integers if they are float
    Returns:
        an integer: the addition of a and b
    """
    if type(a) is not int:
        if type(a) is not float:
            raise TypeError("a must be an integer")
    if type(b) is not int:
        type(b) is not float:
            raise TypeError("b must be an integer")
    else:
        a = int(a)
        b = int(b)
    return int((a + b))


if __name__ == "__main__":
    pass

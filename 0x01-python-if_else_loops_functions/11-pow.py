#!/usr/bin/python3

def pow(a, b):
    prod = 1
    if b >= 0:
        for i in range(b):
            prod = prod * a
    else:
        b = b + (-2 * b)
        for i in range(b):
            prod = prod * a
        prod = 1 / prod
    return prod

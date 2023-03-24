#!/usr/bin/python3

def print_last_digit(number):
    if type(number) == int:
        num = str(number)
        leng = len(num)
        print(num[leng-1], end="")
        return num[leng-1]

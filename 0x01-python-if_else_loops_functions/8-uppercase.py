#!/usr/bin/python3

def uppercase(str):
    strr = ""
    for i in str:
        if ord(i) > 96 and ord(i) < 123:
            i = chr(ord(i) - 32)
            strr += i
        else:
            strr += i
    print(strr)

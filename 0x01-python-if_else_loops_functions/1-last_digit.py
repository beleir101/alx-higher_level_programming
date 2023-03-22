#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
numbe = str(number)
numbe = numbe[-1:]
numbe = int(numbe)
if number >= 0:
    if (numbe < 6) and (numbe != 0):
        print(f"last digit of {number} is {numbe} and is less than 6 and not 0")
    elif (numbe > 5):
        print(f"last digit of {number} is {numbe} and is greater than 5")
    else:
        print(f"last digit of {number} is {numbe} and is 0")
else :
     if (numbe != 0):
        print(f"last digit of {number} is -{numbe} and is less than 6 and not 0")

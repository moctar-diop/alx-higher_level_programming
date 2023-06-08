#!/usr/bin/python3
import random
number = random.randint(-10, 10)
# YOUR CODE HERE
if number % 2:
    print("{} is positive" .format(number))
else:
    print("{} is negative" .format(number))

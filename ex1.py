#!/usr/bin/env python
# ex1.py
import sys

"""
Author: Santhosh Kokala
Date: 03/23/2015

Problem Statement:
-----------------
Define a function max() that takes two numbers as arguments and returns the
largest of them. Use the if-then-else construct available in Python. (It is
true that Python has the max() function built in, but writing it yourself is
nevertheless a good exercise.)

"""

def max(first, second):
    if first > second:
        return first
    else:
        return second

def main():
    # Test inputs for max() function
    print max(1,2)
    print max(3,1)
    print max(-1,4)
    print max(-1,-2)

if __name__ == "__main__":
    sys.exit(main())

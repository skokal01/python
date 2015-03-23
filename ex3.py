#!/usr/bin/env python
# ex3.py

"""
Author: Santhosh
Date: 03/23/2015

Problem Statement:
-----------------
Define a function that computes the length of a given list or string. (It is
true that Python has the len() function built in, but writing it yourself is
nevertheless a good exercise.)

"""

def length(a):
    return sum(1 for n in a)

def main():
    # Test inputs for max() function
    print length("abcdef")
    print length("")
    print length([1,2,3,4,5,6])
    print length([])

if __name__ == "__main__":
    import sys
    sys.exit(main())

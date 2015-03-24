#!/usr/bin/env python
# ex9.py

"""
Author: Santhosh
Date: 03/23/2015

Problem Statement:
-----------------
Write a function is_member() that takes a value (i.e. a number, string, etc) x
and a list of values a, and returns True if x is a member of a, False
otherwise. (Note that this is exactly what the in operator does, but for the
sake of the exercise you should pretend Python did not have this operator.)
"""

def is_member(a, l):
    return any(val == a for val in l)

def main():
    # Test inputs for max() function
    print is_member('a', ['a','b','c'])
    print is_member('d', ['a','b','c'])
    print is_member(1, [1,2,3,])
    print is_member(4, [1,2,3,])

if __name__ == "__main__":
    import sys
    sys.exit(main())

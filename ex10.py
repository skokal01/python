#!/usr/bin/env python
# ex10.py

"""
Author: Santhosh
Date: 03/23/2015

Problem Statement:
-----------------
Define a function overlapping() that takes two lists and returns True if they
have at least one member in common, False otherwise. You may use your
is_member() function, or the in operator, but for the sake of the exercise, you
should (also) write it using two nested for-loops.
"""

def overlapping(l1, l2):
    for i in l1:
        return any(val == i for val in l2)

def main():
    # Test inputs for max() function
    print overlapping([1,2,3], [3,2,1])
    print overlapping([1,2,3], [4,5,1])
    print overlapping([1,2,3], [4,5,6])

if __name__ == "__main__":
    import sys
    sys.exit(main())

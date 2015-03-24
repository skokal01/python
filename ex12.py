#!/usr/bin/env python
# ex12.py

"""
Author: Santhosh
Date: 03/23/2015

Problem Statement:
-----------------
Define a procedure histogram() that takes a list of integers and prints a
histogram to the screen. For example, histogram([4, 9, 7]) should print the
following:

    ****
    *********
    *******
"""
def print_asterisks(num):
    print ''.join('*' for i in xrange(num))

def histogram(s):
    map(print_asterisks, s)

def main():
    # Test inputs
    histogram([4,7,5])
    histogram([2])


if __name__ == "__main__":
    import sys
    sys.exit(main())

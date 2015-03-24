#!/usr/bin/env python
# ex11.py

"""
Author: Santhosh
Date: 03/23/2015

Problem Statement:
-----------------
Define a function generate_n_chars() that takes an integer n and a character c
and returns a string, n characters long, consisting only of c:s. For example,
generate_n_chars(5,"x") should return the string "xxxxx". (Python is unusual in
that you can actually write an expression 5 * "x" that will evaluate to
"xxxxx". For the sake of the exercise you should ignore that the problem can be
solved in this manner.)
"""

def generate_n_chars(n, c):
    return ''.join(c for i in xrange(n))

def main():
    # Test inputs for max() function
    print generate_n_chars(5, 'x')

if __name__ == "__main__":
    import sys
    sys.exit(main())

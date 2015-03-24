#!/usr/bin/env python
# ex7.py

from ex3 import length
"""
Author: Santhosh
Date: 03/23/2015

Problem Statement:
-----------------
Define a function reverse() that computes the reversal of a string. For
example, reverse("I am testing") should return the string "gnitset ma I".
"""

def reverse(s):
    return ''.join(s[i] for i in xrange(length(s)-1, -1, -1))
    

def main():
    # Test inputs for max() function
    print reverse("I am testing")

if __name__ == "__main__":
    import sys
    sys.exit(main())

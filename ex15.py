#!/usr/bin/env python
# ex15.py

from ex3 import length
from ex13 import max_in_list
"""
Author: Santhosh
Date: 03/23/2015

Problem Statement:
-----------------
Write a function find_longest_word() that takes a list of words and returns the
length of the longest one.
"""

def find_longest_word(l):
    return max_in_list(map(length, l))

def main():
    # Test inputs for max() function
    print find_longest_word(["a","ab","abc","a"])
    print find_longest_word(["a","abc",""])

if __name__ == "__main__":
    import sys
    sys.exit(main())

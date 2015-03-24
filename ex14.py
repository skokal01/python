#!/usr/bin/env python
# ex14.py

from ex3 import length
"""
Author: Santhosh
Date: 03/23/2015

Problem Statement:
-----------------
Write a program that maps a list of words into a list of integers representing
the lengths of the correponding words.
"""

def words_length_list(l):
    return map(length, l)

def main():
    # Test inputs for max() function
    print words_length_list(["a","ab","abc","a"])
    print words_length_list(["a","abc",""])

if __name__ == "__main__":
    import sys
    sys.exit(main())

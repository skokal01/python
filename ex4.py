#!/usr/bin/env python
# ex4.py

"""
Author: Santhosh
Date: 03/23/2015

Problem Statement:
-----------------
Write a function that takes a character (i.e. a string of length 1) and returns
True if it is a vowel, False otherwise.
"""

def is_vowel(a):
    return a in 'aeiou'

def main():
    # Test inputs for max() function
    print is_vowel('a')
    print is_vowel('z')

if __name__ == "__main__":
    import sys
    sys.exit(main())

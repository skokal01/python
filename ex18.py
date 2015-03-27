#!/usr/bin/env python
# ex18.py

from ex17 import is_letter
"""
Author: Santhosh
Date: 03/23/2015

Problem Statement:
-----------------
A pangram is a sentence that contains all the letters of the English alphabet
at least once, for example: The quick brown fox jumps over the lazy dog. Your
task here is to write a function to check a sentence to see if it is a pangram
or not.
"""

def is_pangram(sentence):
    return set(''.join(c for c in sentence if is_letter(c)).lower()) == set('abcdefghijklmnopqrstuvwxyz')

def main():
    # Test inputs for max() function
    print is_pangram("The quick brown fox jumps over the lazy dog")
    print is_pangram("My jocks box, get hard, unzip, quiver, flow.")
    print is_pangram("abc")

if __name__ == "__main__":
    import sys
    sys.exit(main())

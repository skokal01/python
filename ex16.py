#!/usr/bin/env python
# ex16.py

"""
Author: Santhosh
Date: 03/23/2015

Problem Statement:
-----------------
Write a function filter_long_words() that takes a list of words and an integer
n and returns the list of words that are longer than n.
"""

def filter_longest_word(words, filter_size):
    return [w for w in words if len(w) > filter_size]

def find_longest_word(l):
    return max_in_list(map(length, l))

def main():
    # Test inputs for max() function
    print filter_longest_word(["a","ab","abc","acde"], 2)
    print filter_longest_word(["a","abc","", "abcd"], 0)
    print filter_longest_word(["a","abc","", "ab"], 1)

if __name__ == "__main__":
    import sys
    sys.exit(main())

#!/usr/bin/env python
# ex8.py

from ex3 import length
"""
Author: Santhosh
Date: 03/23/2015

Problem Statement:
-----------------
Define a function is_palindrome() that recognizes palindromes (i.e. words that
look the same written backwards). For example, is_palindrome("radar") should
return True.
"""

def is_palindrome(s):
    result = True
    str_len = length(s)
    for i in xrange(0, int(str_len/2)):
        if s[i] != s[str_len-i-1]:
            result = False
            break
    return result

def main():
    # Test inputs for max() function
    print is_palindrome("I am testing")
    print is_palindrome("ABABA")


if __name__ == "__main__":
    import sys
    sys.exit(main())

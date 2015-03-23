#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ex5.py

from ex4 import is_vowel

"""
Author: Santhosh
Date: 03/23/2015

Problem Statement:
-----------------
Write a function translate() that will translate a text into "rövarspråket"
(Swedish for "robber's language"). That is, double every consonant and place an
occurrence of "o" in between. For example, translate("this is fun") should
return the string "tothohisos isos fofunon".

"""

def translate(s):
    return ''.join(c + 'o' + c if not is_vowel(c) else c for c in s)
    
def main():
    # Test inputs for max() function
    print translate('a')
    print translate('ab')
    print translate("this is fun")

if __name__ == "__main__":
    import sys
    sys.exit(main())

#!/usr/bin/env python
# ex17.py

from ex8 import is_palindrome
"""
Author: Santhosh
Date: 03/23/2015

Problem Statement:
-----------------
Write a version of a palindrome recognizer that also accepts phrase palindromes
such as "Go hang a salami I'm a lasagna hog.", "Was it a rat I saw?", "Step on
no pets", "Sit on a potato pan, Otis", "Lisa Bonet ate no basil", "Satan,
oscillate my metallic sonatas", "I roamed under it as a tired nude Maori",
"Rise to vote sir", or the exclamation "Dammit, I'm mad!". Note that
punctuation, capitalization, and spacing are usually ignored.
"""

def is_letter(c):
    return c.lower() in 'abcdefghijklmnopqrstuvwxyz'

def is_palindrome_better(sentence):
    return is_palindrome(''.join(c for c in sentence if is_letter(c)).lower())

def main():
    # Test inputs for max() function
    print is_palindrome_better("Go hang a salami I'm a lasagna hog")
    print is_palindrome_better("Was it a rat I saw?")
    print is_palindrome_better("Step on no pets")
    print is_palindrome_better("Sit on a potato pan, Otis")
    print is_palindrome_better("Lisa Bonet ate no basil")
    print is_palindrome_better("Satan,oscillate my metallic sonatas")
    print is_palindrome_better("I roamed under it as a tired nude Maori")
    print is_palindrome_better("Rise to vote sir")
    print is_palindrome_better("Dammit, I'm mad!")

if __name__ == "__main__":
    import sys
    sys.exit(main())

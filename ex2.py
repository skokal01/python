#!/usr/bin/env python
# ex2.py

import sys
from ex1 import max
"""
Author: Santhosh Kokala
Date: 03/23/2015

Problem Statement:
-----------------
Define a function max_of_three() that takes three numbers as arguments and
returns the largest of them.

"""

def max_of_three(first, second, three):
    largest = max(first, second)
    return max(largest, three)

def main():
    # Test inputs for max() function
    print max_of_three(1,2,3)
    print max_of_three(3,2,1)
    print max_of_three(3,1,2)
    print max_of_three(-1,-2,-3)
    print max_of_three(-3,-2,-1)
    print max_of_three(-3,-1,-2)

if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python
# ex6.py

"""
Author: Santhosh
Date: 03/23/2015

Problem Statement:
-----------------
Define a function sum() and a function multiply_list() that sums and multiplies
(respectively) all the numbers in a list of numbers. For example, sum([1, 2, 3,
4]) should return 10, and multiply_list([1, 2, 3, 4]) should return 24.
"""

def multiply_list(m):
    return reduce(lambda x,y: x*y, m)

def sum_list(s):
   return reduce(lambda x,y: x+y, s)
    
def main():
    # Test inputs for max() function
    print sum_list([1,2,3,4])
    print sum_list([-1,2,-3,4])
    print sum_list([4])

    print multiply_list([1,2,3,4])
    print multiply_list([-1,2,-3,4])
    print multiply_list([4])

if __name__ == "__main__":
    import sys
    sys.exit(main())

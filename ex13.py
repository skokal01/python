#!/usr/bin/env python
# ex13.py

"""
Author: Santhosh
Date: 03/23/2015

Problem Statement:
-----------------
The function max() from exercise 1) and the function max_of_three() from
exercise 2) will only work for two and three numbers, respectively. But suppose
we have a much larger number of numbers, or suppose we cannot tell in advance
how many they are? Write a function max_in_list() that takes a list of numbers
and returns the largest one.
"""

def max_in_list(l):
    result = l[0]
    for i in l[1:]:
        if i > result:
            result = i
    return result

def main():
    # Test inputs for max() function
    print max_in_list([1,2,3,4,5])
    print max_in_list([-1,-2,-3,-4,-5])
    print max_in_list([7,11,0,5,-4])
    print max_in_list(['a','b','c','d'])

if __name__ == "__main__":
    import sys
    sys.exit(main())

#!/usr/bin/env python3
"""Day 9: Recursion 3

Task
----
The goal is to implement a function to calculate the factorial recursively.

Input Format
------------
A single integer 'n' (the factorial argument).

Constraints
-----------
- 1 ≤ n ≤ 12
- The factorial function must use recursion

Sample Input
------------
3

Sample Output
-------------
6
"""

def factorial(n):
    """Recursive calculation of n factorial"""
    if n > 1:
        return n * factorial(n-1)
    else:
        return 1
    
if __name__ == '__main__':
    n = int(input().strip())
    result = factorial(n)
    print(result)

#!/usr/bin/env python3
"""Day 3: Intro to Conditional Statements

Task
----
Given an integer `n`, perform the following conditional actions:
- If `n` is odd, print `Weird`
- If `n` is even and in the inclusive range of 1 to 5, print `Not Weird`
- If `n` is even and in the inclusive range of 6 to 20, print `Weird`
- If `n` is even and greater than 20, print `Not Weird`

Input Format
------------
A single line containing a positive integer `n` in the inclusive interval 
from 1 to 100.

Output Format
-------------
Print `Weird` if the number is weird; otherwise, print `Not Weird`.
"""

if __name__ == '__main__':

    n = int(input().strip())

    if n%2 != 0 or 6 <= n <= 20:
        print("Weird")
    else:
        print("Not Weird")

#!/usr/bin/env python3
"""Day 7: Arrays

Task
----
Given an array A of N integers, print A's elements in reverse order as a single
line of space-separated numbers.

Input Format
------------
The first line contains an integer N (the size of our array).
The second line contains N space-separated integers that describe array's
elements.

Sample Input
------------
4
1 4 3 2

Sample Output
-------------
2 3 4 1
"""

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    out = ' '.join([str(i) for i in reversed(arr)])
    print(out)

#!/usr/bin/env python3
"""Day: Let's Review

Task
----
Given a string `S` of length `N` that is indexed from 0 to `N-1`, print its
even-indexed and odd-indexed characters as 2 space-separated strings on a single
line.

Example: `adbecf` -> `abc def`

Input Format
------------
The first line contains an integer `T` (the number of test cases).
Each of the `T` subsequent lines contains a string `S`.

Constraints
-----------
- 1 <= T <= 10
- 2 <= length of S <= 10000

Sample Input
------------
2
Hacker
Rank

Sample Output
-------------
Hce akr
Rn ak
"""

if __name__ == '__main__':

    T = int(input().strip())
    test_cases = []
    for i in range(T):
        test_cases.append(input())

    for S in test_cases:
        even_chars = ''.join([S[i] for i in range(0, len(S), 2)])
        odd_chars = ''.join([S[i] for i in range(1, len(S), 2)])
        print(f"{even_chars} {odd_chars}")

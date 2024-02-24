#!/usr/bin/env python3
"""Merge the Tools!

Given a string `s` and an integer `k`, where `k` is a factor of `len(s)`, 
split the string in contiguous blocks of length `k`.

Then, print each block, ignoring repeated letters.

Example
-------
s = 'AAABCADDE'
- Three sub-blocks: 'AAA', 'BCA', 'DDE'
- u1 = 'A', u2 = 'BCA', u3 = 'DE'

Input
-----
Two lines: the first with the string `s`, the second with the integer `k`.

Sample Input
------------
AABCAAADA
3

Sample Output
-------------
AB
CA
AD
"""

def merge_the_tools(string: str, k: int) -> None:
    tokens = [string[i:i+k] for i in range(0, len(string), k)]
    for t in tokens:
        u = ''
        for c in t:
            if c not in u: u += c
        print(u)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
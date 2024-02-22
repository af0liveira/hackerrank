#!/usr/bin/env python3
"""Text Wrap

Task
----
Given a string `S` and a width `w`, wrap the string into a paragraph of 
width `w`.
This should be implemented in the function `wrap`, which should return 
the wrapped paragraph as a single string.

Sample Input
------------
ABCDEFGHIJKLIMNOQRSTUVWXYZ
4

Sample Output
-------------
ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ
"""

import textwrap

def wrap(string: str, max_width: int) -> str:
    return textwrap.fill(string, max_width)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
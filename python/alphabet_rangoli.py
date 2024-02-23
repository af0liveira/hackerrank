#!/usr/bin/env python3
"""Alphabet Rangoli

Task
----
Print an alphabet rangoli of size N, whre N is an integer.
The center of the rangoli has the first alphabet letter 'a', and the boundary 
has the N-th alphabet letter.

Input Format
------------
Only one line of input containing the size of the rangoli

Sample Input
------------
5

Sample Output
-------------
--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------
"""
import string

def print_rangoli(size: int) -> None:
    chars = list(string.ascii_lowercase[:size])
    lw = 4*size - 3
    for i in range(1-size, size):
        line = '-'.join(chars[:abs(i):-1] + chars[abs(i):])
        print(line.center(lw, '-'))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
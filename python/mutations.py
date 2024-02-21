#!/usr/bin/env python3
"""Mutations

Task
----
Read a given string, change the character at a given index, and then print 
the modified string.
The operation should be implemented in the function `mutate_string`, which 
must return the modified string.

Sample Input
------------
abracadabra
5 k

Sample Output
-------------
abrackdabra
"""

def mutate_string(string: str, position: int, character: str) -> str:
    return string[:position] + character + string[position+1:]

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
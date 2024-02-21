#!/usr/bin/env python3
"""String Split and Join

Task
----
Given a string, split it on a space delimiter and join using a hyphen.
The operation is realized by the function `split_and_join`, which must 
return the resulting string.

Sample Input
------------
this is a string

Sample Ouptut
-------------
this-is-a-string
"""

def split_and_join(line: str) -> str:
    """Replace blank space betwen characters with a hyphen."""
    return '-'.join(line.split())

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
#!/usr/bin/env python3
"""String Validators

Task
----
Given a string `S`, find out if it contains:
- alphanumeric characters
- alphabetical characters
- digits
- lowercase characters
- uppercase characters

Sample Input
------------
qA2

Sample Output
-------------
True
True
True
True
True
"""
if __name__ == '__main__':
    s = input()
    print(any([c.isalnum() for c in s]))
    print(any([c.isalpha() for c in s]))
    print(any([c.isdigit() for c in s]))
    print(any([c.islower() for c in s]))
    print(any([c.isupper() for c in s]))
#!/usr/bin/env python3
"""Day 16: Exceptions - String to Integer

Task
----
Read a string S and print its integer value; if S cannot be converted to an
integer, print "Bad String".

NOTE: The built-in string-to-integer and exception handling constructs must
be used; i.e., using loops/conditionals is not allowed.

Sample Input 0
--------------
3

Sample Output 0
---------------
3

Sample Input 1
--------------
za

Sample Output 1 
---------------
Bad String

Notes
-----
For this to pass the check on HackerRank, the code cannot be in a
`if __name__ == '__main__'` block as shown here.
"""

if __name__ == '__main__':
    S = input()
    try:
        print(int(S))
    except Exception:
        print("Bad String")
"""Mod Divmod

Read in two integers a and b and print 3 lines:
1. The integer division a//b
2. The module a%b
3. The divmod of a and b, which should return (a//b, a%b)

Sample input
------------

177
10

Sample output
-------------

17
7
(17, 7)
"""

if __name__ == '__main__':
    a = int(input())
    b = int(input())

    print(a//b)
    print(a%b)
    print(divmod(a, b))

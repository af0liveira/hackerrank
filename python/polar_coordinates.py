"""Polar Coordinate"

Given a complex number z, convert it to polar coordinates.

Input format
------------

A single line containing the complex number z.
The complex() function can be used to convert the input a a complex number.

E.g.: '1+2j'

Output format
-------------

Output two lines:
- The value of r
- The value of phi

E.g.:
    2.23606797749979 
    1.1071487177940904

The output should be correct up to 3 decimal places.
"""
from cmath import phase

if __name__ == '__main__':
    z = complex(input().replace(" ", ""))
    r = abs(z)
    phi = phase(z)
    print(r)
    print(phi)
    
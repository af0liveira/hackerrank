"""Find Angle MBC

Consider a triangle ABC, with a circumscribed triangle MBC.
The MB segment is orthogonal to the AC segment of the larger triangle;
thus, MBC is a right triangle with BC as its hypotenuse, and BMC angle of 
90 degrees.
The task is to obtain the angle MBC from the length of the AB and BC segments.

Input format
------------

The first line is the length of the side AB.
The second line is the length of the side BC

Output format
-------------

The value of the MBC angle in degress, rounded to the nearest integer.

Sample input
------------
10
10

Sample output
-------------

45°
"""

from math import asin, pi, sqrt, degrees

if __name__ == '__main__':
    ab_length = float(input())
    bc_length = float(input())

    assert 0 < ab_length <= 100, "AB length out of range!"
    assert 0 < bc_length <= 100, "BC length out of range!"

    theta = pi/2 - asin(bc_length/sqrt(ab_length**2 + bc_length**2))
    theta_degrees = degrees(theta)
    print(f"{theta_degrees:.0f}{chr(176)}")
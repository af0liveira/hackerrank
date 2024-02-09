"""Integers Come In All Sizes

Task
----

Read four numbers, a, b, c, and d, and print the result of a**b + c**d.

Input format
------------

Integers a, b, c, and d are given on four separate lines, respectively.

Constraints
-----------

The integers must be in the interval [1, 1000].

Output format
-------------

The result must be printed on one line.

Sample input
------------

9
29
7
27

Sample output
-------------

4710194409608608369201743232
"""

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())

    for i in (a, b, c, d):
        assert 1 <= i <= 1000, "Integer out of range!"

    print(a**b + c**d)

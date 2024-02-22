"""Designer Door Mat

Task
----
Output the design pattern for a N x M mat, such that
- N is an odd number and M = 3N
- the word 'WELCOME' is written in the center
- the design patter only uses `|`, `.`, and `-` characters

Sample Input
------------
9 27

Sample Output
-------------

------------.|.------------
---------.|..|..|.---------
------.|..|..|..|..|.------
---.|..|..|..|..|..|..|.---
----------WELCOME----------
---.|..|..|..|..|..|..|.---
------.|..|..|..|..|.------
---------.|..|..|.---------
------------.|.------------
"""

if __name__ == '__main__':
    n, m = (int(x) for x in input().split())

    deco = '.|.'

    # Print the top half
    for i in range(1, n, 2):
        print((deco*i).center(m, '-'))

    # Print the middle line
    print('WELCOME'.center(m, '-'))

    # Print the bottom half
    for i in range(n-2, 0, -2):
        print((deco*i).center(m, '-'))
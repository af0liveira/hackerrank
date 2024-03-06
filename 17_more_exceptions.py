#!/usr/bin/env python3
"""Day 17: More Exceptions

Task
----
Write a `Calculator` class with a single method: `power(int, int)`.
The `power()` method takes 2 integers, `n` and `p`, and returns the result of
`n` to the power of `p`.
If either `n` or `p` is negative, the method must throw and exception with the
message
"n and p should be non-negative"

Input Format
------------
The first line contains an integer `T` corresponding to the number of test
cases.
Each of the `T` subsequent lines describes a test case in 2 space-separated
integers representing `n` and `p`, respectively.

Sample Input
------------
4
3 5
2 4
-1 -2
-1 3

Sample Output
-------------
243
16
n and p should be non-negative
n and p should be non-negative
"""

#Write your code here
class Calculator:

    def power(self, n: int, p: int) -> int:
        """Return n to the power of p"""
        assert (n >= 0 and p >= 0), "n and p should be non-negative"
        return n**p


myCalculator = Calculator()

T=int(input())
for i in range(T):
    n, p = map(int, input().split())
    try:
        ans = myCalculator.power(n, p)
        print(ans)
    except Exception as e:
        print(e)

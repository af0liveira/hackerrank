#!/usr/bin/env python3
"""Day 19: Interfaces

Task
----
The `AdvancedArithmetic` interface and the method declaration for the abstract
`divisorSum(n)` method are provided.

Complete the implementation of the `Calculator` class, which implements the
`AdvancedArithmetic` interface.
The implementation of the `divisorSum(n)` method must return the sum of all
divisors of `n`.

Input Format
------------
A single line with an integer n, such that 1 ≤ n ≤ 1000.

Sample Input
------------
6

Sample Output
-------------
I implemented: AdvancedArithmetic
12

Explanation
-----------
The integer 6 is evenly divisible by 1, 2, 3, and 6.
Out `divisorSum` method should return the sum of these numbers, i.e., 12.
The `Solution` class then prints `I implemented: AdvancedArithmetic` on the
first line, followed by the sum returned by `divisorSum` on the second line.
"""


class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError


class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        sum = 0
        for d in range(1, n+1):
            if n % d == 0:
                sum += d
        return sum


n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)

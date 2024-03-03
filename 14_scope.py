#!/usr/bin/env python3
"""Day 14: Scope

Task
----
Complete the Difference class by writing the following:

* A constructor that takes an array of integers as a parameter and saves it
  to the `__elements` instance variable.
* A computeDifference method that finds the maximum absolute difference
  between any 2 numbers in __elements and stores it in the maximumDifference
  instance variable.

Sample Input
------------
3       # `__elements` size (N = 3)
1 2 5   # __elements = [1, 2, 5]

Sample Output
-------------
4
"""

class Difference:
    def __init__(self, a: list[int]) -> None:
        self.__elements = a

	# Add your code here
    def computeDifference(self) -> None:
        self.maximumDifference = max(self.__elements) - min(self.__elements)
# End of Difference class

if __name__ == '__main__':
    _ = input()
    a = [int(e) for e in input().split(' ')]

    d = Difference(a)
    d.computeDifference()

    print(d.maximumDifference)
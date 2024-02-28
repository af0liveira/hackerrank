#!/usr/bin/env python3
"""Day 10: Binary Numbers

Task
----
Given a base-10 integer n, convert it to base-2, then find and print the 
base-10 integer denoting the maximum number of consecutive `1`'s in n's 
binary representation.

Note: When working with different bases, it's common to show the base as
a subscript; e.g. 125_{10} is 1111101_{2}.

Constraints
-----------
1 ≤ n ≤ 1_000_000

Input Format
------------
A single integer n.

Sample Input 1
--------------
5

Sample Output 1
---------------
1

Sample Input 2
--------------
13

Sample Output 2
---------------
2

Explanation
-----------
- 5_{10} = 101_{2};   thus, only 1 consecutive 1's
- 13_{10} = 1101_{2}; thus, up to 2 consecutive 1's
"""

if __name__ == '__main__':

    n = int(input().strip())

    n_binary = bin(n)

    one_sequences = str(n_binary)[2:].split('0')

    max_sequence_size = max(map(len, one_sequences))
    print(max_sequence_size)
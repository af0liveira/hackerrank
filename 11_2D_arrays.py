#!/usr/bin/env python3
"""Day 11: 2D Arrays

Task
----
Calculate the hourglass sum for every hourglass in a 2D array A, then print 
the maximum hourglass sum.

Constraints
-----------
- -9 ≤ A[i][j] ≤ 9
- 0 ≤ i,j ≤ 5  (i.e., 6x6 array)

Context
-------
Given a 6x6 2D array A:

1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0 
0 0 0 0 0 0 
0 0 0 0 0 0 

we define an hourglass in A as any subset of values with indices falling in 
this pattern:

a b c
. d .
e f g

The hourglass sum is the sum of the elements in an hourglass.

Example
-------
The array A above, the maximum hourglass sum is the one on the top left 
corner, which adds up to 7.

Sample Input
------------
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0

Sample Output
-------------
19

Explanation
-----------
The sample input contins the following hourglasses:

1 1 1     1 1 0     1 0 0     0 0 0
  1         0         0         0
1 1 1     1 1 0     1 0 0     0 0 0

0 1 0     1 0 0     0 0 0     0 0 0
  1         1         0         0
0 0 2     0 2 4     2 4 4     4 4 0

1 1 1     1 1 0     1 0 0     0 0 0
  0         2         4         4
0 0 0     0 0 2     0 2 0     2 0 0

0 0 2     0 2 4     2 4 4     4 4 0
  0         0         2         0
0 0 1     0 1 2     1 2 4     2 4 0
"""

if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    all_sums = []
    for i in range(6-2):
        for j in range(6-2):
            hourglass_sum = sum(arr[i][j:j+3]) \
                             + arr[i+1][j+1] \
                             + sum(arr[i+2][j:j+3])
            all_sums.append(hourglass_sum)

    print(max(all_sums))
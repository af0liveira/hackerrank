#!/usr/bin/env python3
"""Day 20: Sorting

Task
----
Sort an array `a` of size `n` using the Bubble Sort algorithm. All array
elements are distinct.
Once sorted, the following 3 lines should be printed:
1. "Array is sorted in numSwaps swaps."
   where `numSwaps` is the number of swaps that took place
2. "First Element: firstElement"
   where `firstElement` is the first element in the sorted array
3. "Last Element: lastElement"
   where `lastElement`is the last element in the sorted array

Input Format
------------
The first line contains the number of array elements `n`
The second line contains `n` space-separated integers, the array elements

Constraints
-----------
* 2 ≤ n ≤ 600
* 1 ≤ a[i] ≤ 2e6, where 0 ≤ i < n

Sample Input 0
--------------
3
1 2 3

Sample Output 0
---------------
Array is sorted in 0 swaps.
First Element: 1
Last Element: 3

Sample Input 1
--------------
3
3 2 1

Sample Output 1
---------------
Array is sorted in 3 swaps.
First Element: 1
Last Element: 3
"""


if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    # Write your code here
    num_swaps = 0
    for i in range(n):
        traversal_swaps = 0
        for j in range(n-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                traversal_swaps += 1
        num_swaps += traversal_swaps
        if traversal_swaps == 0:
            break

    print(f"Array is sorted in {num_swaps} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[-1]}")

"""Triangle Quest 2

You are given an integer N.
Your task is to print a palindromic triangle of size N.

E.g.: a palindromic triangle of size 5 is

1
121
12321
1234321
123454321

You can't use more than 2 lines!

Constraints
-----------

0 < N < 10
"""

for i in range(1, int(input())+1):
    print((10**(i)//9)**2)

# Logic
# -----
# 
# We need to obtain the square of numbers containing only the digit 1:
#  1 * 1 = 1
#  11 * 11 = 121
#  111 * 111 = 12321
#  ...
#
# We use the integer portion of divisions by 9 to get such numbers:
#  10**1 // 9 =   10 // 9 =  1   (  10/9 =   1.1111)
#  10**2 // 9 =  100 // 9 =  11  ( 100/9 =  11.1111)
#  10**3 // 9 = 1000 // 9 = 111  (1000/9 = 111.1111)
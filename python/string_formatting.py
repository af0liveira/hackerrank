"""String Formatting

Task
----
Implement the function `print_formatted(number)`, which prints all numbers 
from 1 to `number` (inclusive) in the following formats:

1. Decimal
2. Octal
3. Hexadecimal (capitalized)
4. Binary

The four representations should be printed on a single line, separated by a
single space. Each representation should occupy the space needed for the 
binary value of `number`.

Sample Input
------------
17

Sample Output
-------------
    1     1     1     1
    2     2     2    10
    3     3     3    11
    4     4     4   100
    5     5     5   101
    6     6     6   110
    7     7     7   111
    8    10     8  1000
    9    11     9  1001
   10    12     A  1010
   11    13     B  1011
   12    14     C  1100
   13    15     D  1101
   14    16     E  1110
   15    17     F  1111
   16    20    10 10000
   17    21    11 10001
"""

def print_formatted(number: int) -> None:
    w = len(f"{number:b}")
    for i in range(1, number+1):
        print(f"{i:{w}d} {i:{w}o} {i:{w}X} {i:{w}b}")

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
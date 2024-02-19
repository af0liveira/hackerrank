"""Day 1: Data types

Task
----

Complete the code, which has the variables `i`, `d`, and `s` initialized.
The code should continue as follows:

1. Declare 3 variables of types int, double, and string, respectively.
2. Read 3 lines of input from `stdin` and initialize your 3 variables
3. Use the `+` operator to perform the following operations:
    1. Print the sum of `i` and your int variable on a new line
    2. Print the sum of `d` and your double variable to a scale of one decimal
        on a new line
    3. Concatenate `s` with the string you read as input and print the result 
        on a new line

Sample Input
------------

12
4.0
is the best place to learn and practice coding!

Sample Output
-------------

16
8.0
HackerRank is the best place to learn and practice coding!
"""

i = 4
d = 4.0
s = 'HackerRank '

# Declare second integer, double, and String variables.
# AFO: this isn't needed in Python!

# Read and save an integer, double, and String to your variables.
i2 = int(input())
d2 = float(input())
s2 = input()

# Print the sum of both integer variables on a new line.
print(i + i2)

# Print the sum of the double variables on a new line.
print(d + d2)

# Concatenate and print the String variables on a new line
# The 's' variable above should be printed first.
print(s + s2)
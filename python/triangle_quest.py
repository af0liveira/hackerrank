"""Triangle Quest

You are given a positive integer N.
Print a numerical triangle of height N-1 like the one below:

1
22
333
4444
55555
...

Do it with only arithmetic operations in one for-loop and a print statement.
"""
for i in range(1, int(input())):
    print(i * (10**(i)//9))
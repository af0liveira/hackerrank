"""Tuples
Task
----
Given an integer, , and  space-separated integers as input, create a tuple, t,
of those  integers. Then compute and print the result of hash(t).
"""
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    t = tuple(integer_list)
    print(hash(t))

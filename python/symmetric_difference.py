"""Symmetric Difference
Given  sets of integers, M and N, print their symmetric difference in ascending
order.
The term symmetric difference indicates those values that exist in
either M or N but do not exist in both.
"""
if __name__ == '__main__':
    M = int(input())
    a = map(int, input().split())
    N = int(input())
    b = map(int, input().split())
    
    for i in sorted(set(a)^set(b)):
        print(i)

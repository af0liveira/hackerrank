"""itertools.product()
You are given a two lists A and B.
Your task is to compute their Cartesian product A x B.
"""
import itertools

if __name__ == '__main__':
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    cartesian_product = itertools.product(A, B)
    print(*cartesian_product, sep=' ')

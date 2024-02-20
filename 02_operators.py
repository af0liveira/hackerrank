#!/usr/bin/env python3
"""Day 2: Operators

Task
----
Given the meal price (base cost of a meal), tip percent (the percentage of the
meal price being added as tip), and tax percent (the percentage of the meal
price being added as tax) for a meal, find and print the meal's total cost.
Round the result to the nearest integer.
This should be implemented in the `solve` function.

Sample Input
------------
12.00
20
8

Sample Output
-------------
15

Notes
-----
1. The imports below were part of the initial code provided; however, the
    solution proposed here does not use any of these libraries.
2. Since the function has to print the total cost, but not return it, it 
    should suffice to use f-strings to round the result instead of using the
    `round` instruction.
"""

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function accepts following parameters:
#  1. DOUBLE meal_cost
#  2. INTEGER tip_percent
#  3. INTEGER tax_percent
#

def solve(meal_cost: float, tip_percent: int, tax_percent: int) -> None:
    """Calculates and prints the total cost of a meal, including tip and tax.

    Per requirement, the total cost must be rounded to the nearest integer.

    Parameters
    ----------
    meal_cost: base-cost of the meal
    tip_percent: percentage of base-cost added as tip
    tax_percent: percentage of the base-cost added as tax
    """

    total_cost = meal_cost + meal_cost*(tip_percent+tax_percent)/100
    print(f"{total_cost:.0f}")


if __name__ == '__main__':
    meal_cost = float(input().strip())

    tip_percent = int(input().strip())

    tax_percent = int(input().strip())

    solve(meal_cost, tip_percent, tax_percent)
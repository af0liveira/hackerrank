#!/usr/bin/env python3
"""Capitalize!

Task
----
You are asked to ensure that the first and last names of people begin with a
capital letter in their passports. For example, 'alison heck' should be
capitalised correctly as 'Alison Heck'.
Given a full name, your task is to capitalize the name appropriately.

Note: in a word only the first character is capitalized. Example '12abc', 
when capitalized, remains '12abc'.

Sample Input
------------
chris alan

Sample Output
-------------
Chris Alan
"""

import math
import os
import random
import re
import sys

def solve(s: str) -> str:
    # NOTE: s.title() does not work because it would turn '3ab` into `3Ab`,
    # which is not allowed. The number of spaces between the words cannot be
    # modified either!
    return ' '.join([w.capitalize() for w in s.split(' ')])

if __name__ == '__main__':
    s = input()
    result = solve(s)
    print(result)
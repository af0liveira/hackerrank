#!/usr/bin/env python3
"""What's Your Name?

Task
----
Given the first and last name of a person on two different lines, read them 
and print the following:

"Hello `firstname` `lastname`! You just delved into python."

Input Format
------------
The first line contains the first name, and the second line contains the 
last name.

Sample Input
------------
Ross
Taylor

Sample Output
-------------
Hello Ross Taylor! You just delved into python.
"""

def print_full_name(first: str, last: str) -> None:
    print(f"Hello {first} {last}! You just delved into python.")

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)
#!/usr/bin/env python3
"""Find a string

Task
----
Given a string and substring, print the number of times that the substring
occurs in the given string.
String traversal will take place from left to right, not from right to left.

NOTE: String letters are case-sensitive.

Sample Input
------------
ABCDCDC
CDC

Sample Output
-------------
2 
"""

def count_substring(string: str, sub_string: str) -> int:
    """Find the number of sub_string occurrences in string."""
    count = 0
    for i in range(len(string)):
        if string[i:i+len(sub_string)] == sub_string:
            count += 1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
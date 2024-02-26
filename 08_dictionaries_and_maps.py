#!/usr/bin/env python3
"""Day 8: Dictionaries and Maps

Task
----
Given n names and phone numbers, assemble a phone book that maps friends' 
names to their respective phone numbers. You will then be given an unknown
number of names to query your phone book for. For each name queried, print 
the associated entry from your phone book on a new line in the form 
`name=phone_number`; if an entry for a name is not found, print `Not found`
instead.
Note: Your phone book should be a dictionary/map/hasmap data structure.

Input Format
------------
The first line contais an integer n, denoting the number of entries in the 
phone book.
Each of the n subsequente lines describes an entry in the form of two
space-separated values on a single line; the first value is a friend's name, 
the second is an 8-digit phone number.

After the n lines of phone book numbers, there are an unknown number of lines 
of queires. Each line contains a name to look up, and you must continue 
reading the lines until there is not more input.
Note: Names consist of lowercase English alphabetic letters and are first 
names only.

Constraints
-----------
- 1 <= n <= 100_000
- 1 <= queries <= 100_000

Sample Input
------------
3
sam 99912222
tom 11122222
harry 12299933
sam
edward
harry

Sample Output
-------------
sam=99912222
Not found
harry=12299933
"""

if __name__ == '__main__':

    n = int(input().strip())
    phone_book = {}
    for _ in range(n):
        name, number = input().strip().split()
        phone_book.update({name: number})

    while True:
        try:
            query = input().strip()
        except EOFError:
            break
        else:
            if not query: break

        response = phone_book.get(query)
        if response is not None:
            print(f"{query}={response}")
        else:
            print("Not found")

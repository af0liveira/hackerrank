#!/usr/bin/env bash
"""The Minion Game

Kevin and Stuart want to play 'The Minion Game'.

Game Rules
----------
Both players are given the same string `S`.

Both players have to make substrings of `S`, but
- Stuart's substrings must start with consonants
- Kevin's substrings must start with vowels

The game ends when both players have made all possible substrings of `S`.

Scoring
-------
A player gets 1 point for each occurrence of the substring in `S`.

The occurrences can be overlapping.
E.g.: S = 'BANANA'
- The substring 'ANA' occurs twice, so it gets 2 points for Kevin.
- Note that `str.count()` does not work because it only considers
non-overlapping ocurrences of substrings!

Constraints
-----------
- `S` only contains uppercase letters: [A-Z]
- 0 < len(S) <= 1_000_000

Prints
------
The program should print the winner's name and score, sparated by a space on
one line, or `Draw` if there is no winner.

Sample Input
------------
BANANA

Sample Output
-------------
Stuart 12
"""

def minion_game(string: str) -> None:
    VOWELS: str = 'AEIOU'
    CONSONANTS: str = 'BCDFGHJKLMNPQRSTVWXYZ'

    kevin_score: int = 0
    stuart_score: int = 0
    string_size = len(string)

    for i in range(string_size):
        char = string[i]
        if char in VOWELS:
            kevin_score += string_size - i
        if char in CONSONANTS:
            stuart_score += string_size - i 

    if kevin_score > stuart_score:
        print(f"Kevin {kevin_score}")
    elif kevin_score < stuart_score:
        print(f"Stuart {stuart_score}")
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)
#!/usr/bin/env python3
"""Day 18: Queues and Stacks

Task
----
Determine whether a input string is a palindrome using a queue and stack.

Write the following declarations and implementations:
1. Two instance variables, one for a _stack_ and the other for a _queue_
2. A void `pushCharacter(char ch)` method that pushes a character onto a stack
3. A void `enqueueCharacter(char ch)` method that enqueues a character into the
   queue instance variable
4. A char `popCharacter()` method that pops and returns the character at the
   top of the stack
5. A char `dequeueCharacter()` method that dequeues and returns the first
   character in the queue.

Sample Input
------------
racecar

Sample Output
-------------
The word, racecar, is a palindrome.

Note
----
Except for the Solution class, the code was provided by HackerRank.
"""


class Solution:
    # Write your code here
    def __init__(self):
        self.queue = []
        self.stack = []

    def pushCharacter(self, char: str) -> None:
        """Push char onto the stack."""
        self.stack.append(char)

    def popCharacter(self) -> str:
        """Pop and return the character at the top of the stack."""
        return self.stack.pop()

    def enqueueCharacter(self, char: str) -> None:
        """Enqueue char into the queue."""
        self.queue.append(char)

    def dequeueCharacter(self) -> str:
        """Dequeue and return the first character in the queue."""
        return self.queue.pop(0)


# read the string s
s = input()
# Create the Solution class object
obj = Solution()

length = len(s)
# push/enqueue all the characters of string s to stack
for i in range(length):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])

isPalindrome = True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
'''
for i in range(length//2):
    if obj.popCharacter() != obj.dequeueCharacter():
        isPalindrome = False
        break

# finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, "+s+", is a palindrome.")
else:
    print("The word, "+s+", is not a palindrome.")

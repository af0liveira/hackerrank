#!/usr/bin/env python
"""Day 15: Linked List

Task
----
A Node class is provided. A Node object has an integer data field, `data`,
and a Node instance pointer, `next`, poining to another node (i.e., the next
element of the list).
A node insert function is also declared; it has two parameters, `head` and
`data`, which are a pointer to the first node of the list and the value to
be inserted at the end of the list as a new node.

The task is to implement the insert function so that it creates a new Node
(pass `data` as the Node constructor argument) and inserts it at the tail of
the linked list referenced by the `head` parameter.
Once the new node is added, return the reference to the `head` node.

NOTE: The `head` argument is null for an empty list.

Input Format
------------
The first line contains T, the number of elements to insert.
Each of the next T lines contains an integer to insert at the end of the list.

Sample Input
------------
4       # T = 4
2       # first data = 2
3
4
1       # fourth data = 1

Sample Output
-------------
2 3 4 1
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None 


class Solution: 
    def display(self, head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next

    def insert(self, head, data): 
    #Complete this method
        if head is None:
            return Node(data)

        current = head
        while current.next:
            current = current.next
        current.next = Node(data)

        return head

if __name__ == '__main__':
    mylist= Solution()
    T=int(input())
    head=None
    for i in range(T):
        data = int(input())
        head = mylist.insert(head, data)    
    mylist.display(head); 	  
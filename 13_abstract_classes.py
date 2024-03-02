#!/usr/bin/env python3
"""Day 13: Abstract Classes

Task
----
Given two classes, Book and Solution, write a MyBook class that does the 
following:

* Inherits from Book
* Has a parameterized constructor taking these 3 parameters:
    1. string `title`
    2. string `author`
    3. integer `price`
* Implements the Book class's abstract `display()` method, so it prints these
  3 lines:
    1. "Title:", a space, then the current instance's `title`
    2. "Author:", a space, then the current instance's `author`
    3. "Price:", a space, then the current instance's `price`

NOTE: Because these classes are being implemented in the same file, you must
not use an access modifier (e.g., public) when declaring MyBook, otherwise
your code will not execute.

Sample Input
------------
The Alchemist
Paulo Coelho
24

Sample Output
-------------
Title: The Alchemist
Author: Paulo Coelho
Price: 248

Notes
-----
Except for MyClass, the whole code was provided for the challenge.
The only changed made to the original code was the enclosure of the main
block in the `if __name__ == '__main__'` statement.
"""

from abc import ABCMeta, abstractmethod


class Book(object, metaclass=ABCMeta):

    def __init__(self, title, author):
        self.title = title
        self.author = author   

    @abstractmethod
    def display(): pass


#Write MyBook class
class MyBook(Book):

    def __init__(self, title: str, author: str, price: int) -> None:
        super().__init__(title, author)
        self.price = price

    def display(self) -> None:
        print(f"Title: {self.title}",
              f"Author: {self.author}",
              f"Price: {self.price}",
              sep='\n')
    

if __name__ == '__main__':
    title=input()
    author=input()
    price=int(input())
    new_novel=MyBook(title,author,price)
    new_novel.display()

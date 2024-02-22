#!/usr/bin/env python3
"""Day 4: Class vs. Instance

Task
----
Write a `Person` class with an instance variable `age` and a constructor that
takes an integer `initialAge` as parameter.
The constructor assigns `initialAge` to the `age` attribute if it is not
negative, otherwise, it attributes 0 and prints 
'Age is not valid, setting age to 0.'.

In addition, the following instance methods must be implemented:

1. `yearPasses()` should increase `age` attribute by 1.

2. `amIOld()` should print:
    - 'You are young.' if `age` is less than 13
    - 'You are a teenager.' if `age` is less than 18 but larger or equal to 13
    - 'You are old.' if `age` is 18 or larger

Input Format
------------
The input takes the number of test cases, then the initial age for each test
case in subsequent lines

Sample Input
------------
4
-1
10
16
18

Sample Output
-------------
Age is not valid, setting age to 0.
You are young.
You are young.

You are young.
You are a teenager.

You are a teenager.
You are old.

You are old.
You are old.
"""

class Person:
    def __init__(self, initialAge: int) -> None:
        if initialAge < 0:
            print("Age is not valid, setting age to 0.")
            self.age = 0
        else:
            self.age = initialAge
        
    def amIOld(self) -> None:
        if self.age < 13:
            msg = 'You are young.'
        elif 13 <= self.age < 18:
            msg = 'You are a teenager.'
        else:
            msg = 'You are old.'
        print(msg)

    def yearPasses(self) -> None:
        self.age += 1

# The code below was provided in the challenge and should not be modified!
t = int(input())
for i in range(0, t):
    age = int(input())         
    p = Person(age)  
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()       
    p.amIOld()
    print("")
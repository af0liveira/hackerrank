#!/usr/bin/env python3
"""Day 12: Inheritance

Task
----
Given two classes, Person and Student, where Person is the parent class of
Student, the task is to complete the Student class with the following:

- A constructor with 4 parameters
    1. A string, `firstName`
    2. A string, `lastName`
    3. An integer, `idNumber`
    4. An integer array of test scores, `scores`

- A char `calculated()` method that calculates a Student object's 
averagege and returns the grade character representation of their 
calculated average:

Letter | Average (a)
------ | -----------
O      | 90 ≤ a ≤ 100
E      | 80 ≤ a < 90
A      | 70 ≤ a < 80
P      | 55 ≤ a < 70
D      | 40 ≤ a < 55
T      | a < 40

Input Format
------------
The provided stub code takes care of reading the input and calling the method
for the average calculation.

1st line: firstName lastName idNumber
2nd line: number of test scores
3rd line: space-separated scores

Sample Input
------------
Heraldo Memelli 8135627
2
100 80

Sample Output
-------------
Name: Memelli, Heraldo
ID: 8135627
Grade: O

Note
----
The type hints were not part of the code provided; I added them myself,
just for fun.
"""

class Person:

	def __init__(self, firstName: str, lastName:str, idNumber: str) -> None:
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber

	def printPerson(self) -> None:
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)


class Student(Person):
    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
	def __init__(self, firstName: str, lastName: str, id: str,
			     scores: list[int]) -> None:
		super().__init__(firstName, lastName, id)
		self.scores = scores

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
	def calculate(self) -> str:
		avg = sum(self.scores) / len(self.scores)
		if 90 <= avg <= 100:
			return 'O'
		elif 80 <= avg < 90:
			return 'E'
		elif 70 <= avg < 80:
			return 'A'
		elif 55 <= avg < 70:
			return 'P'
		elif 40 <= avg < 55:
			return 'D'
		elif avg < 40:
			return 'T'
		else:
			raise Exception(f"Value out of expected range: {avg}")
		

if __name__ == '__main__':
    line = input().split()
    firstName = line[0]
    lastName = line[1]
    idNum = line[2]
    numScores = int(input()) # not needed for Python
    scores = list( map(int, input().split()) )
    s = Student(firstName, lastName, idNum, scores)
    s.printPerson()
    print("Grade:", s.calculate())
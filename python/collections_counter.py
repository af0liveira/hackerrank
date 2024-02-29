"""collections.Counter()

Task
----
Raghu has a shoe shop. His shop has X number of shoes.

He has a list containing the size of each shoe he has in his shop.

There are N number of customers who are willing to pay x[i] amount of money
only if they get the shoe of their desired size.

The task is to compute how much money Raghu earned.

Input Format
------------
- 1st line: X, the number of shoes
- 2nd line: space-separated list of all the shoe sizes in the shop
- 3rd line: N, the number of customers
- The next N lines contain the space separated values of the shoe size
  desired by the customer and x[i], the price of the shoe.

Output Format
-------------
Print the amount of money earned by Raghu.

Sample Input
------------
10
2 3 4 5 6 8 7 6 5 18
6
6 55
6 45
6 55
4 40
18 60
10 50

Sample Output
-------------
200
"""
from collections import Counter

if __name__ == '__main__':

    n_shoes = int(input().strip())
    shoe_numbers = Counter(map(int, input().split()))
    
    customer_orders = []
    n_customers = int(input().strip())
    for _ in range(n_customers):
        customer_orders.append(tuple(map(int, input().split())))

    total_earned = 0
    while len(customer_orders) > 0:
        size, payment = customer_orders.pop(0)
        if shoe_numbers.get(size):
            total_earned += payment
            shoe_numbers[size] -= 1

    print(total_earned)
        
"""
    Topic: Assingment 3 Question 9
    Date: 10 Oct 2023
    Author: Kathleen
    
"""

list = [10, 20, 30, 10, 20, 40, 50] 

counter = {}

for value in list:
    if value in counter:
        counter[value] += 1
    else:
        counter[value] = 1

print(counter)

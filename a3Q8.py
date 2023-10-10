"""
    Topic: Assingment 3 Question 8
    Date: 10 Oct 2023
    Author: Kathleen
    
"""

string = "pynativepynvepynative"

counter = {}

for char in string:
    if char in counter:
        counter[char] += 1
    else:
        counter[char] = 1

print (counter)
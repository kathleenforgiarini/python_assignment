"""
    Topic: Assingment 3 Question 2
    Date: 10 Oct 2023
    Author: Kathleen
    
"""
sampleList = ['a', 'c', 'b', 'd', 'd', 'a', 'e', 'a', 'e']

counter = {}

for char in sampleList:
    if char in counter:
        counter[char] += 1
    else:
        counter[char] = 1

print (counter)
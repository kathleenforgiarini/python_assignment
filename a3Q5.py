"""
    Topic: Assingment 3 Question 5
    Date: 10 Oct 2023
    Author: Kathleen
    
"""

rollNumber = [47, 64, 69, 37, 76, 83, 95, 97]
sampleDict = {'Jhon': 47, 'Emma': 69, 'Kelly': 76, 'Jason': 97}

output = set()

for number in rollNumber:
    if number in sampleDict.values():
        output.add(number)

print(f"Output: {output}")

"""
    Topic: Assingment 3 Question 7
    Date: 10 Oct 2023
    Author: Kathleen
    
"""

sampleList = [87, 45, 41, 65, 94, 41, 99, 94]

T1 = tuple(set(sampleList))

min_number = min(T1)
max_number = max(T1)

print(f"Tuple: {T1}")
print(f"Minimum Number: {min_number}")
print(f"Maximum Number: {max_number}")

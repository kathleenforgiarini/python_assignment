"""
    Topic: Assingment 3 Question 6
    Date: 10 Oct 2023
    Author: Kathleen
    
"""

speed ={'jan':47, 'feb':52, 'march':47, 'April':44, 'May':52, 'June':53, 'july':54, 'Aug':44, 'Sept':54}    

L1 = []

for value in speed.values():
    if value not in L1:
        L1.append(value)

print (L1)
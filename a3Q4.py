"""
    Topic: Assingment 3 Question 4
    Date: 10 Oct 2023
    Author: Kathleen
    
"""
firstSet = {27, 43, 34} 
secondSet = {34, 93, 22, 27, 43, 53, 48} 

print (f"First set : {firstSet}")
print (f"Second set: {secondSet}")

if firstSet.issubset(secondSet):
    print("\nThe firstSet is a subset of secondSet")
    firstSet.clear()

elif secondSet.issubset(firstSet):
    print("\nThe secondSet is a subset of firstSet")
    secondSet.clear()

else:
    print("\nNeither set is a subset of the other.")
    
print (f"First set : {firstSet}")
print (f"Second set: {secondSet}")


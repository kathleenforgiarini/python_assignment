"""
    Topic: Assingment 3 Question 1
    Date: 10 Oct 2023
    Author: Kathleen
    
"""

L1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print("\nList:")
print(L1)

parts = len(L1) // 3

chunks = []

for i in range(0, len(L1), parts):
    chunk = L1[i:i+parts]
    chunks.append(chunk)

print("\nSlicing into 3 chunks")
print (chunks)

print("\nEach chunk in normal order:")
for chunk in chunks:
    chunk.sort()
    print (chunk)

print("\nEach chunk in reverse order:")
for chunk in chunks:
    chunk.reverse()
    print (chunk)

chunks.reverse()
print("\nChunks in reverse order:")
print(chunks)
'''
Q. Given two integer arrays of equal length, merge them into one by taking the 
minimum value at the each index.
Example:
Inputs: [1, 2, 3, 4, 5] and [5, 4, 3, 2, 1]
Output:[1, 2, 3, 2, 1] // at the index 0, 1 is smaller than 5. Thus, take 1 as 
the first element.
'''

def solution(a1, a2):
    return [min(i, j) for i, j in zip(a1, a2)]
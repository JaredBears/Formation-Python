'''
Q. Given an array of integers where all but one adjacent pair has been swapped (unsorted), 
fix the array by swapping back the broken pair.

Example:
Input: [1, 2, 3, 5, 4, 6]
Output: [1, 2, 3, 4, 5, 6]
'''

def solution(array):
    i = 0
    while i < len(array) - 1:
        if array[i] > array[i+1]:
            array[i], array[i+1] = array[i+1], array[i]
            i += 2
        else:
            i += 1
    return array
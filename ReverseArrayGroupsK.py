'''
Q. Given an array of integers, reverse the array by blocks of k.
'''

def solution(array, k):
    if k > len(array):
        return array
    i = 0
    j = end = k
    while i < len(array) and i < j:
        while i < j:
            array[i], array[j-1] = array[j-1], array[i]
            i += 1
            j -= 1
        i = end
        j = end = min(end + k, len(array))
    return array
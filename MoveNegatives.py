'''
Q. Given an array of integers, move all negative numbers to 
the left in the order they appear.
'''

def solution(array):
    pref = []
    suff = []
    for num in array:
        if num < 0:
            pref.append(num)
        else:
            suff.append(num)
    return pref + suff
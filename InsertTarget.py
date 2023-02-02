'''
Q. Given a sorted array of integers and a target value, 
insert the target into the array in the appropriate location. 
You may assume there are no duplicates.
'''

def solution(array, target):
    N = len(array)
    if N == 0:
        return [target]
    if N == 1:
        if array[0] >= target:
            return [target, array[0]]
        return [array[0], target]
    end = N
    start = 0
    mid = end // 2
    while start < mid and mid < end:
        if array[mid] > target:
            if array[mid - 1] < target:
                return array[:mid] + [target] + array[mid:]
            start = mid + 1
        elif array[mid] < target:
            if mid + 1 >= N or array[mid + 1] > target:
                return array[:mid+1] + [target] + array[mid+1:]
            end = mid
        elif array[mid] == target:
            return array[:mid] + [target] + array[mid:]
        mid = start + (end - start) // 2
    return array + [target]
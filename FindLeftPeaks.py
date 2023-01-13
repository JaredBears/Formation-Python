from collections import deque
# Find the left peaks in an array
# A peak is a number that is greater than or equal to all numbers to the right.
# In order to solve this problem, we will need to iterate backwards through the array,
# keeping track of the max number we've seen so far.  If the current number is greater
# than or equal to the max number, we will add it to the left peaks array.
# We will then update the max number to be the current number.
# Finally, we will return the left peaks array in reversed order.
# Time Complexity: O(n) where n is the length of the array.
# Space Complexity: O(n)
def findLeftPeaks(array: list[int]) -> list[int]:
    N = len(array)
    left_peaks = []
    max_so_far = float('-inf')
    for i in range(N - 1, -1, -1):
        if array[i] >= max_so_far:
            left_peaks.append(array[i])
            max_so_far = array[i]
    return left_peaks[::-1]

print(findLeftPeaks([1, 2, 5, 3, 1, 2]) == [5, 3, 2])
print(findLeftPeaks([3, 2, 1]) == [3, 2, 1])
print(findLeftPeaks([1,1,1,2,2,2,3,3,3]) == [3, 3, 3])
print(findLeftPeaks([3,2,1,3,2,1]) == [3, 3, 2, 1])
print(findLeftPeaks([1,2,3,1,2,3]) == [3, 3])
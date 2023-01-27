from typing import List
def bubbleSort(array: List[int]) -> List[int]:
    N = len(array)
    swap = True
    while swap:
        swap = False
        for i in range(N-1):
            if array[i] > array[i + 1]:
                swap = True
                array[i], array[i+1] = array[i+1], array[i]
    return array

# Test Cases
print(bubbleSort([])) # []
print(bubbleSort([1])) # [1]
print(bubbleSort([3, 1, 2, 4])) # [1, 2, 3, 4]
print(bubbleSort([-10, 1, 3, 8, -13, 32, 9, 5])) # [-13, -10, 1, 3, 5, 8, 9, 32]
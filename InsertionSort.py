from typing import List

def insertionSort(array: List[int]) -> List[int]:
    N = len(array)
    for i in range(N):
        for j in range(i, N):
            if array[i] > array[j]: 
                array[i], array[j] = array[j], array[i]
    return array

# Test Cases
print(insertionSort([])) # []
print(insertionSort([1])) # [1]
print(insertionSort([3, 1, 2, 4])) # [1, 2, 3, 4]
print(insertionSort([-10, 1, 3, 8, -13, 32, 9, 5])) # [-13, -10, 1, 3, 5, 8, 9, 32]
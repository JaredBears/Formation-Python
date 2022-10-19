from statistics import mean

def averageColumnMinimum(matrix):
    if len(matrix)==0 or len(matrix[0]) == 0:
        return 0
    total = 0
    for j in range(len(matrix[0])):
        minValue = float('inf')
        for i in range(len(matrix)):
            minValue = min (minValue, matrix[i][j])
        total += minValue
    return total / len(matrix[0])

def averageRowMinimum(matrix):
    if len(matrix)==0 or len(matrix[0]) == 0:
        return 0
    total = 0
    for array in matrix:
        minValue = float('inf')
        for i in array:
            minValue = min(minValue, i)
        total += minValue
    return total / len(matrix)

matrix = [[]]
print(averageColumnMinimum(matrix) == 0)
print(averageRowMinimum(matrix) == 0)

matrix = [[5]]
print(averageColumnMinimum(matrix) == 5)
print(averageRowMinimum(matrix) == 5)

matrix = [[1, 2, 3]]
print(averageColumnMinimum(matrix) == 2)
print(averageRowMinimum(matrix) == 1)

matrix = [
  [1],
  [4],
  [7]]
print(averageColumnMinimum(matrix) == 1)
print(averageRowMinimum(matrix) == 4)

matrix = [
  [5, 5, 5],
  [5, 5, 5]]
print(averageColumnMinimum(matrix) == 5)
print(averageRowMinimum(matrix) == 5)

matrix = [
  [32, 23, 3],
  [23,  7, 5]]
print(averageColumnMinimum(matrix) == 11) # average(23, 7, 3) = 11
print(averageRowMinimum(matrix) == 4) # average(5, 3) = 4

matrix = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]]
print(averageColumnMinimum(matrix) == 2)
print(averageRowMinimum(matrix) == 4)

matrix = [
  [ 1,  2,  3,  4,  5],
  [ 6,  7,  8,  9, 10],
  [11, 12, 13, 14, 15]]
print(averageColumnMinimum(matrix) == 3)
print(averageRowMinimum(matrix) == 6)

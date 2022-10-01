def recursiveFactorial(x):
  if x <= 1:
    return 1
  return x * recursiveFactorial(x - 1)

def iterativeFactorial(x):
    i = 1
    result = 1
    while i < x + 1:
        result *= i
        i += 1
    return result


def iterativeMax(arr):
  result = arr[0] if len(arr) > 0 else None

  for i in range(1, len(arr)):
    if arr[i] > result:
      result = arr[i]

  return result

def recursiveMax(arr, curMax=0, i = 0):
  # curMax is an argument that defaults to null if not specified when calling recursiveMax()
  # i is an argument that defaults to 0 if not specified when calling recursiveMax()
  # return null if array is empty
  if(i >= len(arr)):
      return curMax
  return recursiveMax(arr, max(curMax, arr[i]), i+1)

print(iterativeFactorial(0) == 1)
print(iterativeFactorial(1) == 1)
print(iterativeFactorial(3) == 6)
print(iterativeFactorial(4) == 24)
print(iterativeFactorial(10) == 3628800)

print(recursiveMax([4, 2, 7]) == 7)
print(recursiveMax([1, -5, 0, 10]) == 10)
print(recursiveMax([1, 7]) == 7)
print(recursiveMax([1, 0, -5, -3, -6]) == 1)

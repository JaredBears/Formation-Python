def findMin(array):
    minNum = float('inf')
    def helper(idx = 0):
        nonlocal minNum
        if idx >= len(array):
            return
        minNum = min(minNum, array[idx])
        helper(idx + 1)
    helper()
    return minNum

def findMax(array):
    maxNum = float('-inf')
    def helper(idx = 0):
        nonlocal maxNum
        if idx >= len(array):
            return
        maxNum = max(maxNum, array[idx])
        helper(idx + 1)
    helper()
    return maxNum

test = [5,1,4,12,3,-1,10]

print(findMin(test))
print(findMax(test))

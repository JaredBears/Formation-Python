def printAllPairs(array):
    i = 0
    k = len(array)
    while i < k:
        j = i + 1
        while j < k:
            print(array[i], array[j])
            j += 1
        i += 1

testData = [1, 2, 3];

printAllPairs(testData)

def printArray(array):
    i = 0;
    while i < len(array):
        print(array[i])
        i += 1

def printEveryOtherValue(array):
    i = 0;
    while i < len(array):
        print(array[i])
        i += 2

def printEveryOtherValueSkipFirst(array):
    i = 1;
    while i < len(array):
        print(array[i])
        i += 2

def printEveryKth(array, k):
    i = 0;
    while i < len(array):
        print(array[i])
        i += k

def printReverse(array):
    i = len(array) - 1
    while i >= 0:
        print(array[i])
        i -= 1

def printReverseEveryOtherValue(array):
    i = len(array) - 1
    while i >= 0:
        print(array[i])
        i -= 2

def printReverseEveryOtherValueSkipLast(array):
    i = len(array) - 2
    while i >= 0:
        print(array[i])
        i -= 2

def printReverseEveryKth(array, k):
    i = len(array) - 1
    while i >= 0:
        print(array[i])
        i -= k

testData = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


printArray(testData)
printEveryOtherValue(testData)
printEveryOtherValueSkipFirst(testData)
printEveryKth(testData,3)
printReverse(testData)
printReverseEveryOtherValue(testData)
printReverseEveryOtherValueSkipLast(testData)
printReverseEveryKth(testData,3)

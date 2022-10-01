def sumToKTwoPointer(array, k):
    i = 0
    j = len(array) - 1
    while i < j:
        if(array[i] + array[j] == k):
            return True
        elif(array[i] + array[j] < k):
            i += 1
        else:
            j -= 1
    return False

def sumToKFindAllPairs(array, k):
    i = 0
    end = len(array)
    while i < end:
        j = i + 1
        while j < end:
            if(array[i] + array[j] == k):
                return True
            j += 1
        i += 1
    return False

testArrayOne = [1, 5, 8, 10, 13, 18];
testArrayTwo = [1, 5, 5, 11];
testArrayThree = [1, 7, 8];
testArrayFour = [1];
testArrayFive = [ ];

print(sumToKTwoPointer(testArrayOne, 15))
print(sumToKTwoPointer(testArrayTwo, 15))
print(sumToKTwoPointer(testArrayThree, 15))
print(sumToKTwoPointer(testArrayFour, 15))
print(sumToKTwoPointer(testArrayFive, 15))
print(" ")
print(sumToKFindAllPairs(testArrayOne, 15))
print(sumToKFindAllPairs(testArrayTwo, 15))
print(sumToKFindAllPairs(testArrayThree, 15))
print(sumToKFindAllPairs(testArrayFour, 15))
print(sumToKFindAllPairs(testArrayFive, 15))

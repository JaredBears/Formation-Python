def reverseArray(array):
    i = 0
    j = len(array) - 1

    while i < j:
        temp = array[i]
        array[i] = array[j]
        array[j] = temp
        i += 1
        j -= 1
    return array

testData = [1, 2, 3, 4, 5]
testTwoData = ['J', 'A', 'R', 'E', 'D']

print(reverseArray(testData))
print(reverseArray(testTwoData))

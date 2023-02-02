def reverseArray(array):
    return array[::-1]

def reverseArrayLogic(array):
    # This is to practice the logic of reversing an array
    # instead of using built-in functions
    i = 0
    j = len(array) - 1

    while i < j:
        array[i], array[j] = array[j], array[i]
        i += 1
        j -= 1
    return array

testData = [1, 2, 3, 4, 5]
testTwoData = ['J', 'A', 'R', 'E', 'D']

print(reverseArray(testData) == reverseArrayLogic(testData))
print(reverseArray(testTwoData) == reverseArrayLogic(testTwoData))
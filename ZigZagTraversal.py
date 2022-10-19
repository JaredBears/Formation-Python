def zigZag(matrix):
    answer = []
    for i, array in enumerate(matrix):
        if i % 2 == 0:
            for i in array:
                answer.append(i)
        else:
            i = len(array) -1
            while i >= 0:
                answer.append(array[i])
                i -= 1
    return answer;

testMatrix = [[]]
print(zigZag(testMatrix))

testMatrix = [
[1,2,3]
]
print(zigZag(testMatrix))

testMatrix = [
[1],
[6],
[7],
[12]
]
print(zigZag(testMatrix))

testMatrix = [
[1,2,3],
[6,5,4],
[7,8,9],
]
print(zigZag(testMatrix))

testMatrix = [
[1,2,3],
[6,5,4],
[7,8,9],
[12,11,10]
]
print(zigZag(testMatrix))

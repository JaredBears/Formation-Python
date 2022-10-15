def everyXth(input, x):
    answer = []
    i = x - 1
    while i < len(input):
        answer.append(input[i])
        i += x
    return answer

testOne = [1,2,3,4,5,6]

testTwo = everyXth(testOne, 2)

print(testTwo)

print(everyXth(testTwo, 3))

print(everyXth(testTwo, 4))

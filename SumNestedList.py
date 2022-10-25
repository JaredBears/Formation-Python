def sumNestedList(nestedList):
    answer = 0
    for i in range(len(nestedList)):
        if isinstance(nestedList[i], list):
            answer += sumNestedList(nestedList[i])
        else:
            answer += nestedList[i]
    return answer

print(sumNestedList([1, [2,3]])==6)
print(sumNestedList([1, [2, 3, [4]], 5, [6]])==21)
print(sumNestedList([-1, -5, [4], [5], [6, 7]])==16)

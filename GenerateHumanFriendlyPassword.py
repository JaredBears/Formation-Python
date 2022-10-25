def generateAllHumanFriendlyPasswords(words: list[str], maxLength: int) -> list[str]:
    answer = []
    stack = []
    used = {}
    length = 0
    def addWord():
        nonlocal length
        if length > maxLength:
            return
        if length > 0:
            answer.append(" ".join(stack))
        for w in words:
            if not used.get(w):
                stack.append(w)
                used[w] = True
                chars = len(w)
                if length == 0:
                    length = chars
                else:
                    chars +=1
                    length += chars
                addWord()
                stack.pop()
                length -= chars
                used[w] = False

    addWord()
    return answer

testOne = []
testTwo = ["apple", "dog", "banana", "cat"]
testThree = ["zebra", "hammer", "giraffe", "porcupine", "surf"]

print(generateAllHumanFriendlyPasswords(testOne, 0))
print(generateAllHumanFriendlyPasswords(testTwo, 15))
print(generateAllHumanFriendlyPasswords(testThree, 12))

def anagram(str):
    answer = []
    if str == None:
        return answer
    if len(str) <=1:
        answer.append(str)
        return answer
    for c in anagram(str[1:]):
        for i in range(len(str)):
            answer.append(c[:i] + str[0:1] + c[i:])
    return answer

def anagramList(input):
    answer = []
    if list == None:
        return answer
    for i in input:
        answer.append(anagram(i))
    return answer


print(anagramList(["cat", "dog"]))

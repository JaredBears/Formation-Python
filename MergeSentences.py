'''
Q. Given two sentences, merge them into one by alternating words separated by a space. Start with a word from the first sentence.

Example:
Inputs: string1: "Happy Birthday", string2: ""Look! I am flying!"
Output: "Happy Look! Birthday I am flying"
'''

def solution(string1, string2):
    if not string1: return string2
    if not string2: return string1
    s1 = string1.split(" ")
    s2 = string2.split(" ")
    answer = []
    i = 0
    j = 0
    while i < len(s1) or j < len(s2):
        if i < len(s1):
            answer.append(s1[i])
            i += 1
        if j < len(s2):
            answer.append(s2[j])
            j += 1
    return " ".join(answer)
'''
Given a string, remove all future occurrences of a character after the first occurrence. However, it should preserve all spaces.

Example:

Input: "I am happy"
Output: "I am hpy"
'''
def solution(string):
    letters = set()
    answer = ""
    for ch in string:
        if ch == " ":
            answer += ch
        elif ch not in letters:
            answer += ch
            letters.add(ch)
    return answer

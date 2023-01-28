'''
Write a function that takes a string as input and returns the string with only the vowels reversed.
Note: The letters "a", "e", "i", "o", and "u" are vowels. The letter "y" is not a vowel.

Example

For s = "hello, world", the output should be
solution(s) = "hollo, werld";
For s = "codesignal", the output should be
solution(s) = "cadisegnol";
For s = "eIaOyU", the output should be
solution(s) = "UOaIye"
'''
def solution(s):
    vowelSet = (["a","e","i","o","u","A","E","I","O","U"])
    index = []
    for i in range(len(s)):
        if s[i] in vowelSet:
            index.append(i)
    start = 0
    end = len(index) - 1
    while start < end:
        i = index[start]
        j = index[end]
        s = s[:i] + s[j] + s[i+1:j] + s[i] + s[j+1:]
        start += 1
        end -= 1
    return s
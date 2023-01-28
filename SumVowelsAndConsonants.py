'''
You are given a string s that consists of only lowercase English letters. 
If vowels ('a', 'e', 'i', 'o', and 'u') are given a value of 1 and consonants
are given a value of 2, return the sum of all of the letters in the input string.

Example

For s = "a", the output should be
solution(s) = 1;

For s = "abcde", the output should be
solution(s) = 8.

The letters in s, converted to 1s and 2s and added together as described above: 
1 + 2 + 2 + 2 + 1 = 8
'''
def solution(s):
    vowels = set(["a","e","i","o","u"])
    answer = 0
    for ch in s:
        if ch in vowels:
            answer += 1
        else:
            answer += 2
    return answer
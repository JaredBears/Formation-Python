'''
Given a string s consisting of Latin letters and digits, change each of its digit to the 
corresponding number of ones.

Example

For s = "abc5bc3", the output should be solution(s) = "abc11111bc111".

We change digit 5 to five ones and digit 3 to three ones.
'''
def solution(s):
    digitMap = {
        "0" : "",
        "1" : "1",
        "2" : "11",
        "3" : "111",
        "4" : "1111",
        "5" : "11111",
        "6" : "111111",
        "7" : "1111111",
        "8" : "11111111",
        "9" : "111111111"
    }
    i = 0
    while i < len(s):
        ch = s[i]
        if ch in digitMap:
            s = s[:i] + digitMap[ch] + s[i+1:]
            i += int(ch)
        else:
            i += 1
    return s
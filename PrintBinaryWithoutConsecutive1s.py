'''
Given an integer maxLen, print all binary strings of size maxLen that don't have 1s next to each other. That is, no string should contain the substring 11, 111, 1111, 11111, etc. You can assume maxLen > 0.
Function Signature:
def printBinaryWithoutConsecutive1s(maxLen: int) -> None:
Target runtime and space complexity:
Time: O(2^n) where n is the length of the binary string. There are n indexes and each index can be either 0 or 1 with some small exceptions
Space: O(n) because the stack can reach n recursive frames before being torn down
Examples:
printBinaryWithoutConsecutive1s(maxLen=2)
00
01
10

printBinaryWithoutConsecutive1s(maxLen=3)
000
001
010
100
101

Approach:
create a helper function, pass an accumulator string.
if previous is zero, call twice (0 and 1)
if previous is one, call once (0)
once string length is maxLen, print accumulated string and return

'''


def printBinaryWithoutConsecutive1sOrig(maxLen):
    def helper(s):
        if len(s) == maxLen:
            print(s)
            return

        if s[-1] == "1":
            helper(s + "0")
        else:
            helper(s + "0")
            helper(s + "1")
    if maxLen == 0:
        return
    helper("0")
    helper("1")


def printBinaryWithoutConsecutive1s(maxLen, s=''):
    if len(s) == maxLen:
        print(s)
        return

    printBinaryWithoutConsecutive1s(maxLen,s+'0')
    if not s or s[-1] != '1': printBinaryWithoutConsecutive1s(maxLen, s+'1')

printBinaryWithoutConsecutive1s(maxLen=2)
print('-'*30)
printBinaryWithoutConsecutive1s(maxLen=3)

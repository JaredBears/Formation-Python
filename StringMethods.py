def swapChars(str, x, y):
    if(x >= len(str) or y >= len(str)):
        return "Invalid input"
    return str[:x] + str[y] + str[x+1:y] + str[x] + str[y+1:]

def insertChars(str, add, x):
    return str[:x] + add + str[x:]

def removeChars(str, rem):
    i = 0
    while i < len(str):
        if str[i]+str[i+1]==rem:
            return str[:i] + str[i+2:]
        i += 1
    return str

def sortString(str):
    return ''.join(sorted(str))

def getSubstring(str, x):
    return str[:x]

print(swapChars("abcd", 0, 2) == "cbad")
print(swapChars("abcd", 1, 2) == "acbd")

print(insertChars("ab", "c", 1) == "acb")
print(insertChars("abcd", "why", 3) == "abcwhyd")

print(removeChars("abcde", "bc") == "ade")
print(removeChars("abcde", "ab") == "cde")

print(sortString("cab") == "abc")
print(sortString("jared") == "adejr")

print(getSubstring("abcd", 2)=="ab")
print(getSubstring("fedcba", 3) == "fed")

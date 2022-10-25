def changePi(word: str)->str:
    def helper(word, idx = 0):
        if idx >= len(word) - 1:
            return word
        if word[idx:idx+2] == "pi":
            word = word[:idx] + "3.14" + word[idx+2:]
        return helper(word, idx+1)
    return helper(word)

print(changePi("xpix") == "x3.14x")
print(changePi("pipi") == "3.143.14")
print(changePi("pip") == "3.14p")

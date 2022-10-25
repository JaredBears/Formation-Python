def addStars(str):
    def helper(str, idx = 1):
        if idx >= len(str):
            return str
        str = str[:idx] + "*" + str[idx:]
        return helper(str, idx + 2)
    return helper(str)

print(addStars("hello")=="h*e*l*l*o")
print(addStars("1234")=="1*2*3*4")
print(addStars("")=="")
print(addStars("a")=="a")

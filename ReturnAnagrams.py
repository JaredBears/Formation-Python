

def anagram(str):
    tmp = []
    if len(str) <=1:
        tmp.append(str)
        return tmp
    else:
        for c in anagram(str[1:]):
            for i in range(len(str)):
                tmp.append(c[:i] + str[0:1] + c[i:])
        return tmp

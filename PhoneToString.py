def phoneToString(phone):
    conversion = [
        [],
        [],
        ["a","b","c"],
        ["d","e","f"],
        ["g","h", "i"],
        ["j","k","l"],
        ["m", "n", "o"],
        ["q", "r", "s"],
        ["t", "u", "v"],
        ["w", "x", "y", "z"]
    ]
    finalAnswer = []
    def helper(answer = "", idx = 0):
        if not phone or idx >= len(phone):
            return answer
        for i in range(idx, len(phone)):
            for c in conversion[int(phone[i])]:
                res = helper(answer + c, idx + 1)
                if res:
                    finalAnswer.append(res)
    helper()
    return finalAnswer

print(phoneToString("52733")[30]=="jared")
print(phoneToString("22")[0]=="aa")

def commaSeperate(input):
    def helper(index = 0):
        if index == len(input)-2:
            return input[index] + " and " + input[index + 1]
        return input[index] + ", " + helper(index + 1)
    if input == None or len(input) == 0: return
    if len(input) == 1: return input[0]
    return helper()

print(commaSeperate(None))
print(commaSeperate([]))
print(commaSeperate(["Bob"]))
print(commaSeperate(["Bob", "Smith"]))
print(commaSeperate(["Bob", "Smith", "Sally"]))
print(commaSeperate(["Bob", "Smith", "Sally", "Jones"]))

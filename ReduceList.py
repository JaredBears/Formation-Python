# Given an array of length n, consolidate the sum created by adding index pairs until there's only a single index.
# Function Signature:
# def reduceSum(input: list[int]) -> int:
# Target runtime and space complexity:
# Time: O(n2) to run through parts of the n length array n times
# Space: O(n) if it is done in place, otherwise O(n2) when creating new arrays
# Examples:
# [1, 2, 3, 4, 5] => 48
# Explanation:
# The next array would be [3, 5, 7, 9] because [1+2, 2+3, 3+4, 4+5]
# The next array would be [8, 12, 16] because [3+5, 5+7, 7+9]
# The next array would be [20, 28] because [8+12, 12+16]
# The final answer would be [48] because [20+28] and there are not enough operands to add

# check if list is 0
    # return 0
# base case: length of the list is 1
    # return list[0]
# iterate through list length - 1
    # append to output arr[i] + arr[i + 1]
# recursively call function with new list


def reduceSum1(input: list[int]) -> int:
    if len(input) == 0:
        return 0
    if len(input) == 1:
        return input[0]
    output = []
    for i in range(len(input) - 1):
        new_num = input[i] + input[i + 1]
        output.append(new_num)
    return reduceSum1(output)

# check if list is 0
    # return 0
# set index to len(list) - 1
# base case: if index = 0
    #return list[0]
# iterate through list through index
    # list[i] += list[i+1]
# index -= 1
# recursively call


def reduceSum(input: list[int]) -> int:
    if len(input) == 0:
        return 0
    def helper(index):
        if index == 0:
            return input[0]
        for i in range(0, index):
            input[i] += input[i + 1]
        return helper(index - 1)
    return helper(len(input)-1)

# Test Cases

print(reduceSum([1,2,3,4,5]) == 48)
print(reduceSum([5]) == 5)
print(reduceSum([]) == 0)
print(reduceSum([1,3,5]) == 12)
print(reduceSum([-5,5]) == 0)
print(reduceSum([-5,5,-5,5]) == 0)
print(reduceSum([-5,5,5,-5]) == 20)

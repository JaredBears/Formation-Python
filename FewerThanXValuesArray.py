def fewerThanTargetDistinct(arr: list[int], target: int) -> bool:
    answer = set()
    def helper(index = 0):
        if len(answer) > target:
            return False
        if index >= len(arr):
            return True
        answer.add(arr[index])
        return helper(index+1)
    return helper()

print(fewerThanTargetDistinct([1,1,1,2,2,3], 2) == False)
print(fewerThanTargetDistinct([1], 0) == False)
print(fewerThanTargetDistinct([], 0) == True)
print(fewerThanTargetDistinct([1,1,1,1,1,1,2,2,2,2,2,3], 3) == True)
print(fewerThanTargetDistinct([1,2,3,4,5], 5) == True)
print(fewerThanTargetDistinct([1,2,3,4,5], 4) == False)

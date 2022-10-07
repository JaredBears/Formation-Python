def powerOfThree(num):
    if(num == 1 or num == 3):
        return True
    elif (num < 3):
        return False
    return solution(num / 3)

def bunnyEarsTwist(bunnies):
    if bunnies == 0:
        return 0
    elif bunnies % 2 == 0:
        return 3 + bunnyEarsTwist(bunnies - 1)
    else:
        return 2 + bunnyEarsTwist(bunnies - 1)

print(bunnyEarsTwist(2) == 5)
print(bunnyEarsTwist(3) == 7)
print(bunnyEarsTwist(5) == 12)

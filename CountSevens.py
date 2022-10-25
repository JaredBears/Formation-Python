def countSevens(n):
    if n < 7:
        return 0
    if n % 10 == 7:
        return 1 + countSevens(n//10)
    else:
        return countSevens(n//10)

print(countSevens(71717))
print(countSevens(6))
print(countSevens(12345689))
print(countSevens(7))

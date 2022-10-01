from collections import deque

def arrayToPalindromeLL(arr):
    if(len(arr) <= 1):
        return arr
    palindrome = deque()
    palindrome.extendleft(arr)
    palindrome.extend(arr[0:len(arr)-1])
    palindrome.rotate(len(arr) - 1)
    return palindrome

arr = [1, 2, 3, 4]
arrTwo = [1]
arrThree = [1, 2, 3]

print(arrayToPalindromeLL(arr))
print(arrayToPalindromeLL(arrTwo))
print(arrayToPalindromeLL(arrThree))

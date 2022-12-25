def breakPalindrome(palindromeStr):
    # Write your code here
    N = len(palindromeStr)
    if N <= 1:
        return "IMPOSSIBLE"
    mid = (N//2)
    for i in range(mid):
        if palindromeStr[i] > "a":
            return palindromeStr[:i] + "a" + palindromeStr[i+1:]
    return "IMPOSSIBLE" 
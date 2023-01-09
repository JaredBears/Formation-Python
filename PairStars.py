# For this problem, we are instructed to insert a * in between any two letters that are the same.
# In order to accomplish this, we will first create an answer variable initialized to the first 
# letter of the string.  We will then iterate through the string, starting with the second character.
# If the current character is the same as the previous character, we will add a * to the answer string.
# We will then add the current character to the answer string.  Finally, we will return the answer string.
# Time Complexity: O(n) where n is the length of the string
# Space Complexity: O(n)
def pairStars(s: str) -> str:
    if len(s) == 0: return ""
    answer = s[0]
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            answer += "*"
        answer += s[i]
    return answer


print(pairStars("hello") == "hel*lo")
print(pairStars("xxyy") == "x*xy*y")
print(pairStars("aaaa") == "a*a*a*a")
print(pairStars("aaab") == "a*a*ab")
print(pairStars("aa") == "a*a")
print(pairStars("a") == "a")
print(pairStars("") == "")
print(pairStars("noadjacent") == "noadjacent")
print(pairStars("abba") == "ab*ba")
print(pairStars("abbba") == "ab*b*ba")
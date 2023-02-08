'''
❓ PROMPT
Given a string and a non-empty substring *sub*, compute recursively the size of the largest substring which starts and ends with the given *sub* string and return its length, including the length of the substrings. When *sub* is multiple characters, they may overlap with each other and share characters.

Example(s)
strDist("catcowcat", "cat") == 9
strDist("catcowcat", "cow") == 3
strDist("cccatcowcatxx", "cat") == 9
strDist("ooowhwhwooo", "whw") == 5
 

🔎 EXPLORE
State your assumptions & discoveries:
 

Create examples & test cases:
 

🧠 BRAINSTORM
What approaches could work? Consider data structures or algorithmic patterns.
Analyze the space & time complexity.
Approach 1:
Time: O()
Space: O()
 

📆 PLAN
High-level outline of approach #: 
 

🛠️ IMPLEMENT
function strDist(word, sub) {
def strDist(word: str,  sub: str) -> int:
 

🧪 VERIFY
Run your examples & test cases.
Methodically analyze and debug issue(s).

'''

def strDist(word: str,  sub: str) -> int:
    subN = len(sub)
    n = len(word)
    first = -1
    last = -1
    for i in range(n - subN + 1):
        if word[i:i+subN] == sub:
            if first == -1:
                first = i
            last = i
    if first == -1: return 0
    return (last + subN) - first

print(strDist("catcowcat", "cat") == 9)
print(strDist("catcowcat", "cow") == 3)
print(strDist("cccatcowcatxx", "cat") == 9)
print(strDist("abccatcowcatcatxyz", "cat") == 12)
print(strDist("ooowhwhwooo", "whw") == 5)
print(strDist("xyx", "x") == 3)
print(strDist("xyx", "y") == 1)
print(strDist("xyx", "z") == 0)
print(strDist("z", "z") == 1)
print(strDist("x", "z") == 0)
print(strDist("", "z") == 0)
print(strDist("hiHellohihihi", "hi") == 13)
print(strDist("hiHellohihihi", "hih") == 5)
print(strDist("hiHellohihihi", "o") == 1)
print(strDist("hiHellohihihi", "ll") == 2)
'''
❓ PROMPT
Given a string that contains exactly 1 pair of parentheses, compute recursively a new string made of only the parentheses and their contents, so "xyz(abc)123" yields "(abc)".

Example(s)
parenBit("xyz(abc)123") == "(abc)"
parenBit("x(hello)") == "(hello)"
parenBit("(xy)1") == "(xy)"
 

🔎 EXPLORE
State your assumptions & discoveries:
 

Create examples & test cases:
parenBit("J(aRe)D") == "(aRe)"
parenBit("()") == "()"
parenBit("a()b") == "()"
 

🧠 BRAINSTORM
What approaches could work? Consider data structures or algorithmic patterns.
Analyze the space & time complexity.
Approach 1: I could use the string.find() method to find both parentheses
Time: O(n) - two passes
Space: O(1)

Approach 2: I could iterate through the string and save the index location
            of both parentheses
Time: O(n) - one pass
Space: O(1)
 

📆 PLAN
High-level outline of approach #: 
initialize two variables, open and close
iterate through the string, saving the open index and the close index + 1
break when finding the close
return the open:close slice of the word
 

🛠️ IMPLEMENT
function parenBit(word) {
def parenBit(word: str) -> str:
 

🧪 VERIFY
Run your examples & test cases.
Methodically analyze and debug issue(s).

'''

def parenBit(word: str) -> str:
    open = 0
    close = 0
    for i in range(len(word)):
        if word[i] == "(":
            open = i
        elif word[i] == ")":
            close = i + 1
            break
    return word[open:close]

print(parenBit("xyz(abc)123") == "(abc)")
print(parenBit("x(hello)") == "(hello)")
print(parenBit("(xy)1") == "(xy)")
print(parenBit("J(aRe)D") == "(aRe)")
print(parenBit("()") == "()")
print(parenBit("a()b") == "()")
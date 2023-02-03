'''
❓ PROMPT
The decimal system uses the digits 0-9, the binary system uses the digits 0 and 1, and the hexadecimal system uses the digits 0-9 and the letters A-F. The ternary system is a base-3 numeral system that uses the digits 0, 1, and 2.

Given an integer, write a function that converts the number into its base-3 representation. Return the result as a string.

Example(s)
convertToBase3(0) === "0"
convertToBase3(1) === "1"
convertToBase3(2) === "2"
convertToBase3(3) === "10"
convertToBase3(4) === "11"
convertToBase3(-5) === "-12
 

🔎 EXPLORE
State your assumptions & discoveries:
 

Create examples & test cases:

6 == 20
9 == 100
 

🧠 BRAINSTORM
What approaches could work? Consider data structures or algorithmic patterns.
Analyze the space & time complexity.
Approach 1:
Time: O()
Space: O()
 

📆 PLAN
High-level outline of approach #: 
 

🛠️ IMPLEMENT
function convertToBase3(number) {
def convertToBase3(number: int) -> str:
 

🧪 VERIFY
Run your examples & test cases.
Methodically analyze and debug issue(s).

'''

def convertToBase3(number: int) -> str:
    if number == 0: return "0"
    negative = False
    if number < 0:
        negative = True
        number = -number
    answer = ""
    while number:
        number, mod = divmod(number, 3)
        answer = str(mod) + answer
    if negative: return "-" + answer
    return answer

print(convertToBase3(0) == "0")
print(convertToBase3(1) == "1")
print(convertToBase3(2) == "2")
print(convertToBase3(3) == "10")
print(convertToBase3(4) == "11")
print(convertToBase3(-5) == "-12")
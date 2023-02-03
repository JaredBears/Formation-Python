'''
❓ PROMPT
A game developer is creating an online, competitive anagram game where friends can play against each other. The game's objective is to create as many anagrams as possible from a random string shown on the screen. Given the challenge word, 'displayedWord', and the user input, 'userWord', determine if the user input a valid anagram. What would your algorithm look like using built-in functions to simplify the implementation, how about without?

An anagram is a word formed by rearranging the letters of another word using all the original letters exactly once. For example, the words 'opts', 'post', 'pots', 'spot', 'stop', and 'tops' are all anagrams of each other.

As a follow-up, the game developer wants to create a custom anagram dictionary in memory to speed up their game performance by getting the list of anagrams for a word in less than O(N) time, where N is the length of the word list. Given a long list of words, create a class to represent the anagram dictionary. Then, implement a method that accepts a word and returns a list of the anagrams.

Example(s)
isAnagram("coat", "taco") == True
isAnagram("steak", "skate") == True
isAnagram("pots", "stop") == True
isAnagram("stop", "taco") == False

dictionary = AnagramDictionary(["pots", "stop", "cat", "act", "tops", "opts", "post", "spot"])
dictionary.getAnagramWords("tac") == ["cat", "act"]
 

🔎 EXPLORE
State your assumptions & discoveries:
 All words will be the exact same length, and will use the same letters each time

Create examples & test cases:
 

🧠 BRAINSTORM
What approaches could work? Consider data structures or algorithmic patterns.  Use dictionary to count characters for both words and compare if the Counters are equivalent
Analyze the space & time complexity.
Approach 1:
Time: O(n) where n is the number of characters
Space: O(n)
 

📆 PLAN
High-level outline of approach #: 
 Create a Counter variable for the display word and the user word
 return true if both counters are equal, else fale

🛠️ IMPLEMENT
def isAnagram(displayedWord: str, userWord: str) -> bool:

Function signature for follow-up:

class AnagramDictionary:
  def __init__(self, words: list[str]):
    pass

  def getAnagramWords(self, word: str) -> list[str]:
    pass
 

🧪 VERIFY
Run your examples & test cases.
Methodically analyze and debug issue(s).

'''

from collections import Counter, defaultdict

def isAnagram(displayedWord: str, userWord: str) -> bool:
    disCount = Counter(displayedWord)
    useCount = Counter(userWord)
    return disCount == useCount

class AnagramDictionary:
    anagramWords = defaultdict(set)
    def __init__(self, words: list[str]):
        for word in words:
            self.anagramWords["".join(sorted(word))].add(word)

    def getAnagramWords(self, word: str) -> set[str]:
        return self.anagramWords["".join(sorted(word))]

print(isAnagram("", ""))
print(isAnagram("a", "") == False)
print(isAnagram("", "a") == False)
print(isAnagram("a", "a"))
print(isAnagram("a", "b") == False)
print(isAnagram("aaab", "abbb") == False)
print(isAnagram("aab", "abb") == False)
print(isAnagram("coat", "taco"))
print(isAnagram("steak", "skate"))
print(isAnagram("pots", "stop"))
print(isAnagram("stop", "taco") == False)
print(isAnagram("steak", "takes"))
print(isAnagram("stare", "taser"))
print(isAnagram("taser", "tears"))
print(isAnagram("taser", "rates"))
print(isAnagram("asd", "qwertyuiop") == False)

dictionary = AnagramDictionary(["pots", "stop", "cat", "act", "tops", "opts", "post", "spot"])
print(dictionary.getAnagramWords("a") == set([]))
print(dictionary.getAnagramWords("tac") == set(["cat", "act"]))
print(dictionary.getAnagramWords("opst") == set(["pots", "stop", "tops", "opts", "post", "spot"]))
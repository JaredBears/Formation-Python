'''
Given a linked list, delete (k) nodes after the middle.
If (n) is the length of the list, the middle node is [n / 2] using zero-based indexing.
Return the head of the modified list.
Function Signature:
function removeKAfterMiddle(head, k)
Target runtime and space complexity:
Time: O(n) to iterate through the N node linked list
Space: O(1) to store a constant number of variables
Examples:
Example 1

1 -> 2 -> 3 -> 4, k = 2
should return 1 -> 2
Example 2

1, k = 0
should return 1 (single element list)
Example 3

2 -> 9 -> 4 -> 1 -> 7, k = 3
should return 2 -> 9 -> 4

slow and fast pointer
move the fast pointer twice as fast as slow
once i have found the middle,
middle = slow
continue looping slow until k nodes past
middle.next = slow
return head
'''
class Node:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

def removeKAfterMiddle(head, k):
    if not head: return
    slow = fast = head
    while fast and fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    middle = slow
    i = 0
    while i <= k and slow:
        slow = slow.next
        i += 1
    middle.next = slow
    return head

def printList(root):
    curr = root
    print("[", end="")
    while curr and curr.next:
        print(curr.val, end=", ")
        curr = curr.next
    if curr:
        print(curr.val, end="]\n")
    else:
        print(None, end="]\n")

testOne = Node(2, Node(9, Node (4, Node(1, Node(7)))))
testTwo = Node(1, Node(7))
testThree = None
testFour = Node(1)
testFive = Node(2, Node(9, Node (4, Node(1, Node(7, Node(8))))))
testSix = Node(2, Node(9, Node (4, Node(1, Node(7, Node(8))))))

printList(removeKAfterMiddle(testOne, 1)) # 2, 9, 4, 7
printList(removeKAfterMiddle(testTwo, 1)) # 1
printList(removeKAfterMiddle(testOne, 3)) # 2, 9
printList(removeKAfterMiddle(testThree, 2)) # None
printList(removeKAfterMiddle(testFour, 3)) # 1
printList(removeKAfterMiddle(testFive, 2)) # 2, 9, 4, 8
printList(removeKAfterMiddle(testSix, 0)) # 2, 9, 4, 1, 7, 8

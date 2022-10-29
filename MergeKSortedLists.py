from collections import deque

class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

def toString(head):
    if not head:
        return "<empty>"

    parts = []
    curr = head
    while curr:
        parts.append(str(curr.val))
        curr = curr.next

    return " -> ".join(parts)

def mkl(lists):
    if not lists or len(lists) == 0:
        return None
    q = deque(lists)
    def helper(nodeOne, nodeTwo):
        newList = ListNode(0, None)
        currOne = nodeOne
        currTwo = nodeTwo
        currNew = newList
        while currOne or currTwo:
            condition = currOne and currTwo
            if (condition and currOne.val <= currTwo.val) or (currOne and not currTwo):
                currNew.next = ListNode(currOne.val, None)
                currOne = currOne.next
            elif (condition and currTwo.val <= currOne.val) or (currTwo and not currOne):
                currNew.next = ListNode(currTwo.val, None)
                currTwo = currTwo.next
            currNew = currNew.next
        q.append(newList.next)
    while len(q) > 1:
        helper(q.popleft(), q.popleft())
    return q.pop()

LL1 = ListNode(-1, ListNode(4, ListNode(5)))
LL2 = ListNode(1, ListNode(3, ListNode(4, ListNode(4))))
LL3 = ListNode(2, ListNode(6))
LL4 = ListNode(1, ListNode(11, ListNode(111)))

print(toString(mkl([LL1])))
print(toString(mkl([LL1, LL2])))
print(toString(mkl([LL1, LL2, LL3])))
print(toString(mkl([LL1, LL2, LL3, LL4])))

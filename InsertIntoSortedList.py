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

def insert(head, target):
    if not head:
        return ListNode(target)
    sentinal = ListNode(0, head)
    curr = sentinal
    while curr:
        if not curr.next:
            curr.next = ListNode(target)
            return sentinal.next
        elif target < curr.next.val:
            temp = curr.next
            curr.next = ListNode(target, temp)
            return sentinal.next
        curr = curr.next
    return sentinal.next


LL1 = ListNode(-1, ListNode(2, ListNode(3, ListNode(4))))
LL1 = insert(LL1, -3)
LL1 = insert(LL1, -2)
LL1 = insert(LL1, 0)
LL1 = insert(LL1, 1)
LL1 = insert(LL1, 5)
print(toString(LL1))

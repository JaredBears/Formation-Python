class Node:
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

def everyKthNode(head, k):
    answer = Node(0, None)
    pointer = answer
    index = 1
    curr = head
    if not head or k == 0:
        return None
    while curr:
        if index == k:
            pointer.next = Node(curr.val, None)
            pointer = pointer.next
            index = 1
        else:
            index += 1
        curr = curr.next
    return answer.next

test = Node(1, Node(3, Node(6, Node(2, Node(8, Node(9))))))

print(toString(everyKthNode(test, 2)))

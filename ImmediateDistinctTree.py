from collections import deque
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def immediateDistinct(root):
    if not root:
        return True
    q = deque([root])
    while q:
        curr = q.popleft()
        if curr.left:
            if curr.left.val == curr.val:
                return False
            q.append(curr.left)
        if curr.right:
            if curr.right.val == curr.val:
                return False
            q.append(curr.right)
    return True

testOne = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))
testTwo = Node(1, Node(2, Node(4), Node(2)), Node(3, Node(6), Node(7)))

print(immediateDistinct(testOne))
print(immediateDistinct(testTwo))

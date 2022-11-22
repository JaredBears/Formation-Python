from collections import deque

class Node:
    def __init__(self, val, left = None, right = None) -> None:
        self.val = val
        self.left = left
        self.right = right


test = Node(30, Node(20, Node(10), Node(25)), Node(40, Node(33), Node(60)))

def kSmallestNode(root, k):
    answer = []
    def helper(node):
        if not node:
            return
        helper(node.left)
        answer.append(node.val)
        helper(node.right)
    helper(root)
    return answer[k-1]

print(kSmallestNode(test, 1) == 10)
print(kSmallestNode(test, 2) == 20)
print(kSmallestNode(test, 4) == 30)
print(kSmallestNode(test, 7) == 60)

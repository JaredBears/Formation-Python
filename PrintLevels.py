from collections import deque
#TODO
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def printLevels(root):
    if not root:
        return
    print(root.val)
    queue = deque([root])
    while queue:
        curr = queue.popleft()
        if curr.left:
            queue.append(curr.left)
            print(curr.left.val, end="")
        if curr.right:
            queue.append(curr.right)
            print(curr.right.val)

list1 = TreeNode(3, TreeNode(2), TreeNode(4))

printLevels(list1)

'''
Q. Given a binary tree, sum all right leaf nodes.
'''
#
# Binary trees are already defined with this interface:
class Tree(object):
  def __init__(self, x):
    self.value = x
    self.left = None
    self.right = None
def solution(root):
    if not root: return 0
    stack = [root]
    total = 0
    while stack:
        curr = stack.pop()
        if curr.right:
            if not curr.right.right and not curr.right.left:
                total += curr.right.value
            else:
                stack.append(curr.right)
        if curr.left:
            stack.append(curr.left)
    return total
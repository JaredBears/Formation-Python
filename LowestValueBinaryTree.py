'''
Q. Given a binary tree, find the node with the lowest value.
'''

#
# Binary trees are already defined with this interface:
class Tree(object):
  def __init__(self, x):
    self.value = x
    self.left = None
    self.right = None
def solution(root):
    if not root: 0
    min_value = float('inf')
    stack = [root]
    while stack:
        curr = stack.pop()
        min_value = min(curr.value, min_value)
        if curr.left: stack.append(curr.left)
        if curr.right: stack.append(curr.right)
    return min_value
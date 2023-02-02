'''
Q. Given a binary tree, count the number of non-leaf nodes (leaf nodes do not have any children).
'''

#
# Binary trees are already defined with this interface:
class Tree(object):
  def __init__(self, x):
    self.value = x
    self.left = None
    self.right = None
def solution(root):
    stack = [root]
    count = 0
    while stack:
        curr = stack.pop()
        if not curr: continue
        if curr.left or curr.right:
            count += 1
            stack.extend([curr.left, curr.right])
    return count

'''
Q. Given a binary tree, count the number of elements with even values in the tree.
'''

#
# Binary trees are already defined with this interface:
class Tree(object):
  def __init__(self, x):
    self.value = x
    self.left = None
    self.right = None
def solution(root):
    count = 0
    if not root: return count
    stack = [root]
    while stack:
        curr = stack.pop()
        if not curr.value % 2:
            count += 1
        if curr.left: stack.append(curr.left)
        if curr.right: stack.append(curr.right)
    return count

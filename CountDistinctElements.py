'''
Q. Given a binary tree, count the number of distinct elements in the tree.

     1
   9   5
  1     3
returns 4.

     6
   6   5
  1   6
returns 3.
'''
#
# Binary trees are already defined with this interface:
class Tree(object):
  def __init__(self, x):
    self.value = x
    self.left = None
    self.right = None
def solution(root):
    elements = set()
    stack = [root]
    while stack:
        curr = stack.pop()
        if not curr: continue
        elements.add(curr.value)
        stack.extend([curr.left, curr.right])
    return len(elements)
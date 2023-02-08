
'''
Q. Given a binary tree, sum all left leaf nodes.
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
    total = 0
    while stack:
        curr = stack.pop()
        if not curr: continue
        if curr.left:
            if not curr.left.left and not curr.left.right:
                total += curr.left.value
            else:
                stack.append(curr.left)
        stack.append(curr.right)
    return total
'''Q. Given a binary tree and a target k, count the number of nodes that has a value larger than k.'''

#
# Binary trees are already defined with this interface:
class Tree(object):
  def __init__(self, x):
    self.value = x
    self.left = None
    self.right = None
def solution(root, k):
    count = 0
    stack = [root]
    while stack:
        curr = stack.pop()
        if not curr: continue
        if curr.value > k: count += 1
        stack.extend([curr.left, curr.right])
    return count
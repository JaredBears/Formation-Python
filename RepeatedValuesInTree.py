'''
Q. Given a binary tree and a target k, return any values in the tree 
that is repeated exactly k times. If multiple values are repeated k 
times, return the smaller value. If there isn't any value repeated k 
times, return -1.
'''
from collections import defaultdict
#
# Binary trees are already defined with this interface:
class Tree(object):
  def __init__(self, x):
    self.value = x
    self.left = None
    self.right = None
def solution(root, k):
    count = defaultdict(int)
    stack = [root]
    while stack:
        curr = stack.pop()
        if not curr: continue
        count[curr.value] += 1
        stack.extend([curr.left, curr.right])
    for key, value in count.items():
        if value == k:
            return key
    return -1
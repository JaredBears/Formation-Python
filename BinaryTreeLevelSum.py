'''
Q. Given a binary tree, return the sum of the level whose values add up to the highest sum.

     5
   2   6
  1 3    8
       17
returns 17.

     51
   2   6
  1 3    8
       17
'''
from collections import deque
#
# Binary trees are already defined with this interface:
class Tree(object):
  def __init__(self, x):
    self.value = x
    self.left = None
    self.right = None
def solution(root):
    if not root: return 0
    max_sum = root.value
    curr_sum = 0
    q = deque([root, None])
    while len(q) > 1:
        curr = q.popleft()
        if curr:
           curr_sum += curr.value
           if curr.left: q.append(curr.left)
           if curr.right: q.append(curr.right)
        else:
            max_sum = max(curr_sum, max_sum)
            curr_sum = 0
            q.append(None)
    return max(max_sum, curr_sum)

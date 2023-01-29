'''
Q. Given the root of a binary tree, return average values of nodes on each level starting from the root in an array form.

     1
   2  3
returns [1, 2.5]

     5
   2   6
  1 3    8
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
    curr_sum = 0
    count = 0
    answer = []
    q = deque([root, None])
    while len(q) > 1:
        curr = q.popleft()
        if curr:
           curr_sum += curr.value
           count += 1
           if curr.left: q.append(curr.left)
           if curr.right: q.append(curr.right)
        else:
            answer.append(curr_sum / count)
            curr_sum = 0
            count = 0
            q.append(None)
    answer.append(curr_sum / count)
    return answer

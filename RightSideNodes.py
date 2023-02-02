'''
Q. Given a binary tree, return the values of the nodes when facing the tree from the right side (from top to bottom).

Example:
Input:
   1              <---
 /   \
2     5         <---
 \  
  7               <---
Output: [1, 5, 7]
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
    q = deque([root, None])
    curr = root
    answer = []
    while q:
        prev, curr = curr, q.popleft()
        while curr:
            if curr.left: q.append(curr.left)
            if curr.right: q.append(curr.right)
            prev, curr = curr, q.popleft()
        answer.append(prev.value)
        if q: q.append(None)
    return answer
            
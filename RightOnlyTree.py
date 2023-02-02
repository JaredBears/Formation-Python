'''
Q. Construct a right child only tree from a given array.

Input: [1, 2, 3]
Output: 
          1
            \
              2
                \
                 3
'''

#
# Binary trees are already defined with this interface:
class Tree(object):
  def __init__(self, x):
    self.value = x
    self.left = None
    self.right = None
def solution(array):
    curr = dummy = Tree(0)
    for num in array:
        curr.right = Tree(num)
        curr = curr.right
    return dummy.right
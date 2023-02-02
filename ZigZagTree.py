'''Q. Construct a zigzag tree from an array (alternating right and left child), starting with right.

Example:
Input: [1, 2, 3, 4, 5]
Output:
          1
            \
              2
             /
          3
            \
              4
             /
          5
'''

#
# Binary trees are already defined with this interface:
class Tree(object):
  def __init__(self, x):
    self.value = x
    self.left = None
    self.right = None
def solution(array):
    right = False
    curr = dummy = Tree(0)
    for num in array:
        if right:
            curr.right = Tree(num)
            curr = curr.right
        else:
            curr.left = Tree(num)
            curr = curr.left
        right = not right
    return dummy.left

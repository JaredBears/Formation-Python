'''Q. Given a binary search tree, return the value of the violating node. When there is a violation, return the lowest node. If there is no violating node, return -1.

The properties of a binary search tree are that:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
A violating node occurs when one of these properties is not met.

For example, in this tree:

      5
    /  \
  2    10
   \
    8
We have a violation between 5 and 8 because 8 is not less than 5. Because 8 is the lower node, return 8.
'''
import math
#
# Binary trees are already defined with this interface:
class Tree(object):
  def __init__(self, x):
    self.value = x
    self.left = None
    self.right = None
def solution(root):
    def findInvalid(node, low=-math.inf, high=math.inf):
        if not node:
            return False
        if node.value <= low or node.value >= high:
            return node.value
        right = findInvalid(node.right, node.value, high)
        left = findInvalid(node.left, low, node.value)
        if right: return right
        if left: return left
    invalid = findInvalid(root)
    if invalid:
        return invalid
    return -1
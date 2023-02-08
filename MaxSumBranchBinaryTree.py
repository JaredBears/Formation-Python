'''Q. Given a binary tree, return the the maximum sum of nodes from the root to any leaf.

For example, in this tree:
1
2 3
4 5 6 7

There are 4 leaves, and thus 4 paths from root to leaf:
1 -> 2 -> 4, 1 -> 2 -> 5, 1 -> 3 -> 6, 1 -> 3 -> 7

The one with the maximum sum is 1 -> 3 -> 7, so return 11.
'''
#
# Binary trees are already defined with this interface:
class Tree(object):
  def __init__(self, x):
    self.value = x
    self.left = None
    self.right = None
def solution(root):
    maxTotal = 0
    def dfs(node, total):
        nonlocal maxTotal
        if not node:
            maxTotal = max(maxTotal, total)
            return
        dfs(node.left, total + node.value)
        dfs(node.right, total + node.value)
    if not root: return 0
    dfs(root, 0)
    return maxTotal
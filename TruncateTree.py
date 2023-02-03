'''
Q. Given a binary tree and a depth, remove all nodes that are lower than that depth.

Function Description
replaceNodeValuesBT has the following parameters:

root: the root of the tree
depth: the max depth. This value will be >= 0

Returns:
The root of the tree
'''
#
# Binary trees are already defined with this interface:
class Tree(object):
  def __init__(self, x):
    self.value = x
    self.left = None
    self.right = None
def solution(root, max_depth):
    def dfs(node, depth):
        if depth >= max_depth:
            node.left = None
            node.right = None
            return
        if node.left: dfs(node.left, depth + 1)
        if node.right: dfs(node.right, depth + 1)
    dfs(root, 0)
    return root
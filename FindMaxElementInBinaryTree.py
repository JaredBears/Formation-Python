class TreeNode:
    def __init__(self, value = 0, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

def tree_max(root: TreeNode):
    # Time: O(n) - one pass
    # Space: O(n)
    # This can be solved with either dfs or bfs, we just need to
    # completely traverse the tree while keeping track of the max
    # value.  We can use a stack for dfs or a queue for bfs.
    if not root: return float("-inf")
    stack = [root]
    max_value = float("-inf")
    while stack:
        curr = stack.pop()
        max_value = max(max_value, curr.value)
        if curr.right: stack.append(curr.right)
        if curr.left: stack.append(curr.left)
    return max_value

# Test Cases
print(tree_max(None) == float("-inf"))
print(tree_max(TreeNode(1, TreeNode(2), TreeNode(3))) == 3)
print(tree_max(TreeNode(2, TreeNode(29, TreeNode(26)), TreeNode(4, None, TreeNode(2, TreeNode(9))))) == 29)
print(tree_max(TreeNode(1)) == 1)
print(tree_max(TreeNode(-10, TreeNode(-20), TreeNode(-30))) == -10)
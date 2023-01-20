from collections import deque
class TreeNode:
    def __init__(self, value = 0, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

def find_dfs(root: TreeNode, target: int) -> bool:
    if not root:
        return False
    q = deque([root])
    while q:
        curr = q.popleft()
        if curr.value == target: return True
        if curr.left: q.append(curr.left)
        if curr.right: q.append(curr.right)
    return False

tree1 = TreeNode(3, TreeNode(29, TreeNode(2)), TreeNode(4, None, TreeNode(2, TreeNode(9))))
print(find_dfs(None, 1) == False)
print(find_dfs(tree1, 9) == True)
print(find_dfs(tree1, 1) == False)
print(find_dfs(tree1, 2) == True)
print(find_dfs(TreeNode(1), 2) == False)
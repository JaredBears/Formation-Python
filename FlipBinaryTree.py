class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def flip(self):
        def helper(node):
            if not node:
                return
            temp = node.left
            node.left = node.right
            node.right = temp
            helper(node.left)
            helper(node.right)
        helper(self)

    def printBinaryTree(self):
        def helper(node):
            if node:
                print(node.val)
                helper(node.left)
                helper(node.right)
        helper(self)

test = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))

test.printBinaryTree();
print("")
test.flip()
test.printBinaryTree()

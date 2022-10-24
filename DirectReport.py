class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isDirectReport(orgChart, personA, personB):
    def helper(node):
        if not node:
            return False
        if node.val == personA:
            if node.left.val == personB or node.right.val == personB:
                return True
        return helper(node.left) or helper(node.right)
    return helper(orgChart)

roger = TreeNode("Roger")
greg = TreeNode("Greg")
jess = TreeNode("Jess")
sam = TreeNode("Sam", jess, greg)
jared = TreeNode("Jared", sam, roger)
nick = TreeNode("Nick")
sharon = TreeNode("Sharon", jared, nick)

orgChart = sharon

print(isDirectReport(orgChart, "Jared", "Sam")) #True
print(isDirectReport(orgChart, "Sharon", "Nick")) #True
print(isDirectReport(orgChart, "Sam", "Roger")) #False
print(isDirectReport(orgChart, "Sam", "Greg")) #True
print(isDirectReport(orgChart, "Jared", "Greg")) #False

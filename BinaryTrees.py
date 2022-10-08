class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def printBinaryTree(root):
    if root:
        print(root.val)
        printBinaryTree(root.left)
        printBinaryTree(root.right)

def iterativeSearchInBST(root, target):
  curr = root
  while curr:
      if(curr.val == target):
          return True
      if(curr.val > target):
          curr = curr.left
      else:
          curr = curr.right
  return False

def recursiveSearchInBST(root, target):
    if(root == None):
        return False
    if(root.val == target):
        return True
    if(root.val > target):
        return recursiveSearchInBST(root.left, target)
    return recursiveSearchInBST(root.right, target)

def insertIntoBST(root, val):
    if(not root):
        return Node(val)
    curr = root
    while curr:
        if(val > curr.val):
            if(curr.right == None):
                curr.right = Node(val)
                return root
            else:
                curr = curr.right
        else:
            if(curr.left == None):
                curr.left = Node(val)
                return root
            else:
                curr = curr.left;

def pruneTree(root):
    if root:
        root.left = pruneTree(root.left)
        root.right = pruneTree(root.right)
        if(root.val or root.left or root.right):
            return root


def sum_tree(root: Node) -> int:
    if not root:
        return 0
    return root.val + sum_tree(root.right) + sum_tree(root.left)

def sum_tree_even(root: Node) -> int:
    if not root:
        return 0
    if root.val % 2 == 0:
        if(root.right and root.left):
            return root.right.val + root.left.val + sum_tree_even(root.right) + sum_tree_even(root.left)
        elif(root.right):
            return root.right.val + sum_tree_even(root.right)
        elif(root.left):
            return root.left.val + sum_tree_even(root.left)
        else:
            return 0
    else:
        if(root.right and root.left):
            return sum_tree_even(root.right) + sum_tree_even(root.left)
        elif(root.right):
            return sum_tree_even(root.right)
        elif(root.left):
            return sum_tree_even(root.left)
        else:
            return 0

def hasSingleChild(root: Node):
    parents = []
    def hasSingleChildHelper(root):
        if not root:
            return
        if((root.left and not root.right) or (root.right and not root.left)):
            parents.append(root.val)
        hasSingleChildHelper(root.left)
        hasSingleChildHelper(root.right)

    hasSingleChildHelper(root)
    return parents


# Test Cases

print(hasSingleChild(None) == [])

root = Node(1)
print(hasSingleChild(root) == [])

#   1
# 2
root = Node(1,
  Node(2))
print(hasSingleChild(root) == [1])

#   1
# 2   3
root = Node(1,
  Node(2),
  Node(3))
print(hasSingleChild(root) == [])

#     1
#  2     3
# _ 4   _ _
root = Node(1,
  Node(2,
    None,
    Node(4)),
  Node(3))
print(hasSingleChild(root) == [2])

#     12
#  3     4
# 1 _   6 _
root = Node(12,
  Node(3,
    Node(1)),
  Node(4,
    Node(6)))
print(hasSingleChild(root) == [3,4])

#     12
#   3     4
#  1 _   6  _
# 9 _   _ _
root.left.left.left = Node(9)
print(hasSingleChild(root) == [3,1,4])

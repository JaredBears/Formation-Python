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

def count_tree(root: Node) -> int:
    if(not root or root == None):
        return 0
    return 1 + count_tree(root.left) + count_tree(root.right)

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

def createParentSumTree(root: Node):
    def helper(root: Node, parentVal: int):
        if(not root or root == None):
            return
        selfVal = root.val
        root.val += parentVal
        helper(root.left, selfVal)
        helper(root.right, selfVal)
    helper(root.left, root.val)
    helper(root.right, root.val)
    return root

def findMostFrequentNodeVal(root: Node):
    max = 0
    maxCount = 0
    map = {}
    def helper(root: Node):
        if not root:
            return
        if root.val in map:
            map[root.val] += 1
        else:
            map[root.val] = 1
        helper(root.left)
        helper(root.right)
    helper(root)

    for k, v in map.items():
        if v > maxCount:
            max = k
            maxCount = v
    return max

def getHeight(root):
    if not root:
        return 0
    leftHeight = getHeight(root.left)
    rightHeight = getHeight(root.right)

    if leftHeight > rightHeight :
        return 1 + leftHeight
    else:
        return 1 + rightHeight

def traverseBFS(root):
    queue = [root]
    while queue:
        curr = queue.pop()
        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)

def getHeightBFS(root):
    if not root:
        return 0
    queue = [root]
    leftHeight = 1
    rightHeight = 1
    while queue:
        curr = queue.pop()
        if curr.left:
            queue.append(curr.left)
            leftHeight += 1
        if curr.right:
            queue.append(curr.right)
            rightHeight += 1
    if leftHeight > rightHeight:
        return leftHeight
    else:
        return rightHeight

# Test Cases

list1 = Node(1, Node(2), Node(4, Node(2, Node(1))))
list2 = Node(1, Node(3, Node(3)), Node(4))
list3 = Node(9)

print(getHeightBFS(list1) == 4)
print(getHeightBFS(list2) == 3)
print(getHeightBFS(list3) == 1)

class Node:
    def __init__(self, val, left = None, right = None) -> None:
        self.val = val
        self.left = left
        self.right = right


def arrayToBST(array) -> Node:
    def helper(idx, edx, node):
        if idx > edx:
            return
        mid = idx + (edx - idx) //2
        node.val = array[mid]
        node.left = Node(None)
        node.right = Node(None)
        helper(idx, mid-1, node.left)
        helper(mid+1, edx, node.right)
    root = Node(None)
    helper(0, len(array) - 1, root)

def isCorrect(r): return b(r) and v(r)
def gH(r):
    if r == None: return 0
    lH=gH(r.left)
    if lH==-1: return -1
    rH=gH(r.right)
    if rH==-1: return -1
    if abs(lH-rH)>1: return -1
    return max(lH,rH)+1
def b(r):return gH(r)!=-1
import sys
def v(r): return vx(r,~sys.maxsize,sys.maxsize)
def vx(r,m,M):
    if r==None: return True
    if r.val>=M or r.val<=m: return False
    return vx(r.left,m,r.val) and vx(r.right,r.val,M)

print(isCorrect(arrayToBST([])))
print(isCorrect(arrayToBST([1])))
print(isCorrect(arrayToBST([1,2])))
print(isCorrect(arrayToBST([1,2,3,4,5])))
print(isCorrect(arrayToBST([1,2,10,20,35,50,420,609])))
print(isCorrect(arrayToBST([-100,-50,-25,-20,-10,-1,0,1,2,10,20])))

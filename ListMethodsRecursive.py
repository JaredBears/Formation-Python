class ListNode:
    def __init__(self, value = 0, next = None):
        self.value = value
        self.next = next

def arrayify(head) -> [int]:
    array = []
    ptr = head
    while ptr != None:
        array.append(ptr.value)
        ptr = ptr.next
    return array

def count(head):
    if(head == None):
        return 0
    return 1 + count(head.next)

def sum(head):
    if(head == None):
        return 0
    return head.value + sum(head.next)

def append(head: ListNode, value: int) -> ListNode:
    if(head == None):
        return ListNode(value)
    return ListNode(head.value, append(head.next, value))

# Test Cases
LL1 = ListNode(1, ListNode(4, ListNode(5)))
print(sum(LL1))
print(arrayify(append(None, 1))) # [1]
print(arrayify(append(LL1, 7))) # [1, 4, 5, 7]
print(arrayify(append(ListNode(), 7))) # [0, 7]

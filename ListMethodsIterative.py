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
    count = 0
    if(head == None ):
        return count
    while head:
        count += 1
        head = head.next
    return count

def sum(head):
    sum  = 0
    if(head == None):
        return sum
    while head:
        sum += head.value
        head = head.next
    return sum


def append(head: ListNode, value: int) -> ListNode:
    if(head == None):
        return ListNode(value)
    curr = head
    while curr.next:
        curr = curr.next
    curr.next = ListNode(value)
    return head

# Test Cases
LL1 = ListNode(1, ListNode(4, ListNode(5)))
print(sum(LL1))
print(arrayify(append(None, 1))) # [1]
print(arrayify(append(LL1, 7))) # [1, 4, 5, 7]
print(arrayify(append(ListNode(), 7))) # [0, 7]

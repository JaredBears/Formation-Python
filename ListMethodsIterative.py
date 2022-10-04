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

def reverseArray(head: ListNode):
    arr = []
    if(head == None):
        return arr
    while head:
        arr.append(head.value)
        head = head.next
    i = 0
    j = len(arr) - 1
    while i < j:
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
        i += 1
        j -= 1
    return arr


# Test Cases
LL1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))

print(reverseArray(LL1))

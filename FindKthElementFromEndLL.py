class ListNode:
    def __init__(self, value = 0, next = None):
        self.value = value
        self.next = next



def kthFromLast(head: ListNode, k: int) -> int:
    slow = fast = head
    i = 0
    while slow and fast:
        if i >= k:
            slow = slow.next
        fast = fast.next
        i += 1
    if i >= k and slow:
        return slow.value
    else:
        return -1



# Test Cases

LL1 = ListNode(13, ListNode(1, ListNode(5, ListNode(3, ListNode(7, ListNode(10))))))

print(kthFromLast(LL1, 1)==10) # 10
print(kthFromLast(LL1, 3)==3) # 3
print(kthFromLast(LL1, 6)==13) # 13
print(kthFromLast(LL1, 7)==-1) # -1

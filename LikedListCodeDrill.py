def arrayToLL(array):
    LL = []
    i = 0
    while i < len(array):
        LL.append(array[i])
        i += 1
    return LL

#TODO does not work in all cases
def insertZeros(head):
    if(head == None):
        return head

    curr = head
    if(curr.next == None):
        curr.next = ListNode(0)
        return head
    previous = curr
    while curr and curr.next:
        temp = curr.next
        newNode = ListNode(0);
        newNode.next = temp
        curr.next = newNode
        previous = curr
        curr = temp.next
    previous.next.next.next = ListNode(0);
    return head

def listOfTarget(target, count):
    LL = []
    i = 0
    while i < count:
        LL.append(target)
        i += 1
    return LL

def firstElementAppearsK(head, k):
    count = {}
    if(head == None):
        return -1
    while head:
        if(head.value in count):
            count[head.value] += 1
        else:
            count[head.value] = 1
        if(count[head.value] >= k):
            return head.value
        head = head.next
    return -1

def removeAllOdds(head):
    while (head is not None) and (head.value % 2 == 1):
        head = head.next
    curr = head
    while (curr is not None) and (curr.next is not None):
        if(curr.next.value % 2 == 1):
            curr.next = curr.next.next
        else:
            curr = curr.next
    return head

def removeElementsRepeatedOverK(head, k):
    count = {}
    if k == 0:
        return []
    if(head == None):
        return head
    curr = head
    count[curr.value] = 1
    while curr.next:
        if(curr.next.value in count):
            count[curr.next.value] += 1
        else:
            count[curr.next.value] = 1
        if count[curr.next.value] > k:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return head

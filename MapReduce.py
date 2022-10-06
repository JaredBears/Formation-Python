'''

function reduce(head, accumulator, initialVal) - returns single value

function map(head, mapper) - returns new list

function any(head, test) - returns true if at least one value passes the test function

function all(head, test) - returns true if ALL of the values in the list pass the test function

BONUS: function filter(head, test) - modifies list and returns new head


test = [1,2,3,4,5]

function add(a, b) {
    return a * b
}

test.reduce(add, 0)

add(0,1) = 1
add(1,2) = 3
3 + 3 = 6
6 + 4 = 10
10 + 5 = 15

return 15

'''

class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

'''
function reduce(head, accumulator, initialVal) - returns single value

first we need write our traversal logic

save results that we get from our accumulator



pass current result into accumulator function with next node

return result


'''
def reduce(head, accumulator, initialVal):
    result = initialVal
    while head:
        result = accumulator(head.value, result)
        head = head.next
    return result
# LL1 = Node(1, Node(2, Node(3, Node(4, Node(5)))) )
# print(reduce(LL1, lambda x, y: x * y, 1))

'''
function map(head, mapper) - returns new list



'''

def map(head, mapper):
    ll = Node()
    cur = ll
    while head:
        cur.next = Node(mapper(head.value))
        cur = cur.next
        head = head.next
    return ll.next

# LL1 = Node(1, Node(2, Node(3, Node(4, Node(5)))) )
# res = map(LL1, lambda x: x**2)

# while res:
#     print(res.value)
#     res = res.next


'''
function any(head, test) - returns true if at least one value passes the test function
'''
def any(head, test):
    while head:
        if test(head.value):
            return True
        head = head.next
    return False

LL1 = Node(1, Node(2, Node(3, Node(4, Node(5)))) )
LL2 = Node(1)
LL3 = Node()

# print(any(LL1, lambda x: x > 3))
# print(any(LL2, lambda x: x > 3))
# print(any(LL3, lambda x: x >= 0))


'''
function all(head, test) - returns true if ALL of the values in the list pass the test function


'''

def all(head, test):
    while head:
        if not test(head.value):
            return False
        head = head.next
    return True

# print(all(LL1, lambda x: x > 3))
# print(all(LL2, lambda x: x > 3))
# print(all(LL3, lambda x: x >= 0))


'''
BONUS: function filter(head, test) - modifies list and returns new head

d -> 1 -> 2 -> 3 -> 4 -> 5



'''

def filter(head, test):
    sentinel = Node()
    sentinel.next = head

    curr = sentinel
    while curr and curr.next:
        if test(curr.next.value) == False:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return sentinel.next



LL1 = Node(1, Node(2, Node(3, Node(4, Node(5)))) )
LL2 = Node(1)
LL3 = Node()
res = filter(LL1, lambda x: x % 2 == 0)

while res:
    print(res.value)
    res = res.next

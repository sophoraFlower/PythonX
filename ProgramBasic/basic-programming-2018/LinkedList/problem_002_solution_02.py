

class Node(object):

    def __init__(self, data, next_=None):
        self.data = data
        self.next_ = next_


head = None
for count in range(1, 6):
    head = Node(count, head)

# while head is not None:
#     print(head.data)
#     head = head.next_


# 反转链表
def reverseList(self, head):
    cur, prev = head, None
    while cur:
        cur.next_, prev, cur = prev, cur, cur.next_
    return prev


def swapPairs(self, head):
    pre, pre.next_ = self, head
    while pre.next_ and pre.next_.next_:
        a = pre.next_
        b = a.next_
        pre.next_, b.bext_, a.next_ = b, a, b.next_
        pre = a
    return self.next_


swapPairs(head)


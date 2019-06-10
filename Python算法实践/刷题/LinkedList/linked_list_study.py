class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node


head = None
for count in range(10):
    head = Node(count, head)
# while head is not None:
#     print(head.data)
#     head = head.next

"""
index = 5
probe = head
while index > 0:
    probe = probe.next
    index -= 1
print(probe.data)
"""


def reverse_linked_list(linked_list):
    if linked_list is None or linked_list.next is None:
        return
    probe = None
    tmp = linked_list.next
    while tmp:
        linked_list = linked_list.next
        tmp.next = probe
        tmp = tmp.next
    return tmp


reverse_linked_list(head)
while head is not None:
    print(head.data)
    head = head.next

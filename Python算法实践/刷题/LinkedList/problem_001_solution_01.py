# 实现链表的逆序

class Node(object):
    """Represents a singly linked node."""

    def __init__(self, data, next = None):
        self.data = data
        self.next = next


head = None
for count in range(1, 10):
    head = Node(count, head)
# while head != None:
#     print(head.data)
#     head = head.next

# 遍历
probe = head
while probe != None:
    print(probe)
    probe = probe.next

# 搜索4
target = head
targetItem = 4
while target != None and targetItem != target.data:
    target = target.next
if target != None:
    print("4 is in")
else:
    print("4 is not in")

# 替换，同遍历，搜索
# 插入操作（开始处、结尾处、中间I）
insertItem = 11
insertIndex = 6
if head is None or insertIndex <=0:
    head = Node(insertItem, head)
else:
    probe = head
    while insertIndex > 1 and probe.next != None:
        probe = probe.next
        insertIndex -= 1
    probe.next = Node(insertItem, probe.next)
probe = head
while probe != None:
    print(probe.data)
    probe = probe.next

# 删除操作（开始处、结尾处、中间I）
def removedItem(index, head):
    if index <= 0 or head.next is None:
        removedValue = head.data
        head = head.next
        return removedValue
    else:
        probe = head
        while index > 1 and probe.next.next != None:
            probe = probe.next
            index -= 1
        removedValue = probe.next.data
        probe.next = probe.next.next
        return removedValue

removedItem(8, head)
probe = head
while probe != None:
    print(probe.data)
    probe = probe.next
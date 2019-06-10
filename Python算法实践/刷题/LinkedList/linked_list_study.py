class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node


head = None
for count in range(3):
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


# 迭代
def reverse_linked_list1(linked_list):
    cur, prev = linked_list, None
    while cur:
        cur.next, prev, cur = prev, cur, cur.next
    return prev


# 递归
def reverse_linked_list2(linked_list):
    if not linked_list or not linked_list.next:
        return linked_list
    else:
        reverse_linked_list = reverse_linked_list2(linked_list.next)
        linked_list.next.next = linked_list
        linked_list.next = None
        return reverse_linked_list


# 常规
def reverse_linked_list3(linked_list):
    pre = linked_list
    cur = linked_list.next
    pre.next = None
    while cur:
        temp = cur.next
        cur.next = pre
        pre = cur
        cur = temp
    return pre


# 常规2
def reverse_linked_list4(linked_list):
    # 将原链表的head节点（第一个节点）变成新链表的最后一个节点
    prev = linked_list
    # 当前链表相当于原链表删除第一个节点
    cur = linked_list.next
    # 新链表的tail节点指向None
    prev.next = None
    while cur:
        # 将cur的下一个节点保存在temp中，也就是第3个节点，因为翻转后，节点2的下一个节点变成了节点1，原先节点2和节点3之间的连接断开，通过节点2就找不到节点3了，因此需要保存
        temp = cur.next
        # 将当前节点的下一个节点指向新链表的第一个节点
        cur.next = prev
        # 新链表head节点的值为原链表当前节点的值
        prev = cur
        # 原链表的当前节点为保存的temp
        cur = temp
    return prev


# reverse_linked_list_ = reverse_linked_list4(head)
# while reverse_linked_list_ is not None:
#     print(reverse_linked_list_.data)
#     reverse_linked_list_ = reverse_linked_list_.next


def swap_pairs(linked_list):
    if not linked_list or not linked_list.next:
        return linked_list
    elif not linked_list.next.next:
        temp = linked_list
        linked_list = linked_list.next
        linked_list.next = temp
        temp.next = None
        return linked_list
    else:
        cur_list = linked_list.next.next
        new_list = swap_pairs(cur_list)
        return new_list


swap_linked_list = swap_pairs(head)
while swap_linked_list is not None:
    print(swap_linked_list.data)
    swap_linked_list = swap_linked_list.next

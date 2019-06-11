class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node


head1 = None
for i in range(1, 6):
    count = 6 - i
    head1 = Node(count, head1)

head2 = None
for j in range(10, 15):
    count = 25 - j
    head2 = Node(count, head2)


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


# 反转链表测试
# reverse_linked_list_ = reverse_linked_list4(head)
# while reverse_linked_list_ is not None:
#     print(reverse_linked_list_.data)
#     reverse_linked_list_ = reverse_linked_list_.next

# 合并两个有序链表
def merge_two_list(h1, h2):
    if h1 is None and h2 is None:
        return None
    elif h1 is None:
        return h2
    elif h2 is None:
        return h1
    elif h1.data <= h2.data:
        h1.next = merge_two_list(h1.next, h2)
        return h1
    else:
        h2.next = merge_two_list(h1, h2.next)
        return h2


head3 = merge_two_list(head1, head2)
# while head3:
#     print(head3.data)
#     head3 = head3.next

# 在两个数据节点之间插入链表
head4 = None
for count in range(6, 11):
    head4 = Node(count, head4)

node_value = 5


def insert_node(data, h1, h2):
    if h1 is None and h2 is None:
        return
    elif h1 is None:
        return h2
    elif h2 is None:
        return h1
    elif h1.data != data:
        h1.next = insert_node(data, h1.next, h2)
        return h1
    else:
        temp = h1.next
        h1.next = h2
        h2.next = insert_node(data, h2.next, temp)
        return h1


head4 = reverse_linked_list1(head4)
head5 = insert_node(node_value, head3, head4)
while head5:
    print(head5.data)
    head5 = head5.next

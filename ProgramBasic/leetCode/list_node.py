class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 在两个节点间添加节点
def between(pre_node, new_data):
    if pre_node is None:
        print("缺插入节点的前一个节点")
        return
    new_node = ListNode(new_data)
    new_node.next = pre_node.next
    pre_node.next = new_node


# 头插入
def create_linked_list_head(li: list):
    # 确定头部节点
    head = ListNode(li[0])
    for ele in li[1:]:
        # 创建节点
        node = ListNode(ele)
        node.next = head
        head = node
    return head


# 尾插入
def create_linked_list_tail(li: list):
    # 确定头部节点
    head = ListNode(li[0])
    # 确定尾部节点
    tail = head
    for ele in li[1:]:
        # 创建节点
        node = ListNode(ele)
        tail.next = node
        tail = node
    return head


# 打印链表
def print_linked_list(ll: ListNode):
    while ll:
        print(ll.val)
        ll = ll.next


def print_linked_list_string(ll: ListNode):
    string_list = []
    while ll:
        string_list.append(ll.val)
        ll = ll.next
    print(sorted(string_list))


# 通过链表计算 9999+123456=133455
def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    if l1 is None:
        return l2
    if l2 is None:
        return l1
    # 创建头节点
    result = ListNode(0)
    p = result
    carry = 0
    while l1 and l2:
        p.next = ListNode((l1.val+l2.val+carry) % 10)
        carry = (l1.val+l2.val+carry) // 10
        l1 = l1.next
        l2 = l2.next
        p = p.next
    if l1:
        while l1:
            p.next = ListNode((l1.val + carry) % 10)
            carry = (l1.val + carry) // 10
            l1 = l1.next
            p = p.next
    if l2:
        while l2:
            p.next = ListNode((l2.val + carry) % 10)
            carry = (l2.val + carry) // 10
            l2 = l2.next
            p = p.next
    if carry == 1:
        p.next = ListNode(1)
    return result.next


lk = create_linked_list_head([1, 2, 3, 4])  # 4 > 3 > 2 > 1
lk_2 = create_linked_list_tail([1, 2, 3, 4])  # 1 > 2 > 3 > 4

print_linked_list(lk)
print_linked_list(lk_2)

# 通过链表计算 9999+123456=133455
l1_ = create_linked_list_head([9, 9, 9, 9])
l2_ = create_linked_list_head([1, 2, 3, 4, 5, 6])

print_linked_list_string(l1_)  # [9, 9, 9, 9]
print_linked_list_string(l2_)  # [1, 2, 3, 4, 5, 6]

ss = addTwoNumbers(l1_, l2_)
print_linked_list_string(ss)  # [1, 3, 3, 4, 5, 5]


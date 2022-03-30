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


lk = create_linked_list_head([1, 2, 3, 4])  # 4 > 3 > 2 > 1
lk_2 = create_linked_list_tail([1, 2, 3, 4])  # 1 > 2 > 3 > 4

print_linked_list(lk)
print_linked_list(lk_2)





class Node:
    """ 节点 """

    def __init__(self, data=None):
        self.data = data  # 数据
        self.next = None  # 指标


def between(pre_node, new_data):
    """ 在链表两个节点间插入新节点 """
    if pre_node is None:
        print("缺插入节点的前一个节点")
        return
    new_node = Node(new_data)
    new_node.next = pre_node.next
    pre_node.next = new_node


class LinkedList:
    """ 链表 """

    def __init__(self):
        self.head = None  # 链表第1个节点

    def print_list(self):
        ptr = self.head  # 指标指向链表第1个节点
        while ptr:
            print(ptr.data)
            ptr = ptr.next

    def begin(self, new_data):
        """ 在第1个节点前插入新节点 """
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def end(self, new_data):
        """ 在链表末端插入新节点 """
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last_ptr = self.head
        while last_ptr.next:
            last_ptr = last_ptr.next
        last_ptr.next = new_node

    def rm_node(self, rm_key):
        """ 删除指定内容的节点 """
        ptr = self.head
        prev = ptr
        if ptr.data == rm_key:
            self.head = ptr.next
            return
        while ptr.next:
            if ptr.data == rm_key:
                break
            ptr = ptr.next
        if ptr is None:
            return
        prev.next = ptr.next


link = LinkedList()
link.head = Node(5)
n2 = Node(15)
n3 = Node(25)
link.head.next = n2
n2.next = n3

link.begin(1)
link.end(45)
between(n3, 35)
link.rm_node(5)
link.rm_node(25)

link.print_list()

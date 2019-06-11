# 双向链表
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, value):
        node = Node(value)
        node.next = self.head
        if self.head is not None:
            self.head.prev = node
        self.head = node

    def list_print(self, node):
        while node is not None:
            print(node.data)
            node = node.next

    def insert(self, prev_node, value):
        if prev_node is None:
            return
        new_node = Node(value)
        # 插入第一个位置进行的操作
        new_node.next = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node
        if new_node.next is not None:
            new_node.next.prev = new_node

    # 附加一个节点到最后,采用递归
    def append(self, node, value):
        if node is None:
            return Node(value)
        elif node.next is None:
            node.next = Node(value)
            Node(value).prev = node
            return node
        else:
            node = self.append(node.next, value)
            return node


dllist = DoublyLinkedList()
dllist.push(8)
dllist.push(88)
dllist.push(888)
# dllist.list_print(dllist.head)  # 888 <> 88 <> 8
dllist.insert(dllist.head.next, 66)
# dllist.list_print(dllist.head)  # 888 <> 88 <> 66 <> 8
dllist.insert(dllist.head, 33)
# dllist.list_print(dllist.head)   # 888 <> 33 <> 88 <> 66 <> 8
dllist.append(dllist.head, 8888)
dllist.list_print(dllist.head)






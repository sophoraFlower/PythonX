class Node:
    """ 节点 """

    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.previous = None


class Double_linked:
    """ 双向链表 """

    def __init__(self):
        self.head = None  # 链表头部的节点
        self.tail = None  # 链表尾部的节点

    def add_double_list(self, new_node):
        if isinstance(new_node, Node):
            if self.head is None:
                self.head = new_node
                new_node.previous = None
                new_node.next = None
                self.tail = new_node
            else:
                self.tail.next = new_node
                new_node.previous = self.tail
                self.tail = new_node
        return

    def print_list_from_head(self):
        ptr = self.head
        while ptr:
            print(ptr.data)
            ptr = ptr.next

    def print_list_from_tail(self):
        ptr = self.tail
        while ptr:
            print(ptr.data)
            ptr = ptr.previous


double_linked = Double_linked()
n1 = Node(5)
n2 = Node(15)
n3 = Node(25)

for n in [n1, n2, n3]:
    double_linked.add_double_list(n)

double_linked.print_list_from_head()
print("-------------")
double_linked.print_list_from_tail()

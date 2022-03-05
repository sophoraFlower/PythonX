class Node:
    """ 节点 """

    def __init__(self, data=None):
        self.data = data  # 数据
        self.next = None  # 指标


class LinkedList:
    """ 链表 """

    def __init__(self):
        self.head = None  # 链表第1个节点

    def linked_list_length(self):
        length = 0
        ptr = self.head
        while ptr:
            length += 1
            ptr = ptr.next
        return length

    def find_key_numbers(self, find_key):
        numbers = 0
        ptr = self.head
        while ptr:
            if ptr.data == find_key:
                numbers += 1
            ptr = ptr.next
        return numbers


link = LinkedList()
print(link.linked_list_length())
link.head = Node(5)
n2 = Node(15)
n3 = Node(5)
link.head.next = n2
n2.next = n3
print(link.linked_list_length())
print("5在链表中出现了：" + str(link.find_key_numbers(5)) + "次")
print("10在链表中出现了：" + str(link.find_key_numbers(15)) + "次")
print("20在链表中出现了：" + str(link.find_key_numbers(20)) + "次")

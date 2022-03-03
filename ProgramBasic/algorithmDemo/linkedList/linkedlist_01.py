class Node:
    """ 节点 """
    def __init__(self, data=None):
        self.data = data  # 数据
        self.next = None  # 指标


n1 = Node(5)  # 节点1
n2 = Node(15)  # 节点2
n3 = Node(25)  # 节点3
n1.next = n2
n2.next = n3
ptr = n1  # 建立指标节点

while ptr:
    print(ptr.data)
    ptr = ptr.next


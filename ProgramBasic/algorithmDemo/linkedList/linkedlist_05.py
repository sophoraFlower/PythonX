class Node:
    def __init__(self, data=None):
        self.data = data
        self.previous = None
        self.next = None


class Doubled_list:
    def __init__(self):
        self.head = None
        self.tail = None

    def print_from_head(self):
        ptr = self.head
        while ptr:
            print(ptr.data)
            ptr = ptr.next

    def print_from_tail(self):
        ptr = self.tail
        while ptr:
            print(ptr.data)
            ptr = ptr.previous


double_list_week = Doubled_list()
n1 = Node("Sun")
n2 = Node("Mon")
n3 = Node("Tue")
n4 = Node("Web")
n5 = Node("Thu")
n6 = Node("Fri")
n7 = Node("Sat")

double_list_week.head = n1
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = n7
double_list_week.tail = n7
n7.previous = n6
n6.previous = n5
n5.previous = n4
n4.previous = n3
n3.previous = n2
n2.previous = n1

double_list_week.print_from_head()
double_list_week.print_from_tail()



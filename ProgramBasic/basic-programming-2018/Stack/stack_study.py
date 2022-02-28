# stack 堆（堆栈），表示将对象放在另一个对象上,后进先出
class Stack:
    def __init__(self):
        self.stack = []

    def add(self, data):
        if data not in self.stack:
            self.stack.append(data)
            return True
        else:
            return False

    # 删除第一个元素
    def peek(self):
        return self.stack[0]

    def remove(self):
        if len(self.stack) <= 0:
            return "No element in the Stack"
        else:
            return self.stack.pop()


a_stack = Stack()
a_stack.add("a")
a_stack.add("b")
print(a_stack)
# print(a_stack.peek())  # a
print(a_stack.remove())  # b






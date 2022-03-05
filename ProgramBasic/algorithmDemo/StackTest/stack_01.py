class Stack:

    def __init__(self):
        self.my_stack = []

    def my_push(self, data):
        self.my_stack.append(data)

    def my_pop(self):
        return self.my_stack.pop()

    def size(self):
        return len(self.my_stack)

    def is_empty(self):
        return self.my_stack == []


stack = Stack()
animals = ["dog", "cat", "pig"]
for animal in animals:
    stack.my_push(animal)

print(stack.size())

while not stack.is_empty():
    print(stack.my_pop())

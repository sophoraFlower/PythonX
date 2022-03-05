class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.insert(0, data)
        print("成功插入 " + data + " 至队列")

    def dequeue(self):
        if len(self.queue):
            return self.queue.pop()
        return "队列是空的"


q = Queue()
q.enqueue("Grape")
q.enqueue("Apple")
q.enqueue("Mango")

print("读取队列：", q.dequeue())
print("读取队列：", q.dequeue())
print("读取队列：", q.dequeue())
print("读取队列：", q.dequeue())

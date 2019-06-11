# Queue 先进先出，如排队
class Queue:
    def __init__(self):
        self.queue = list()

    def addtop(self, data):
        if data not in self.queue:
            self.queue.insert(0, data)
            return True
        return False

    def size(self):
        return len(self.queue)

    def removefromq(self):
        if len(self.queue) <= 0:
            return "No elements in Queue!"
        else:
            return self.queue.pop()


queue1 = Queue()
queue1.addtop("a")
queue1.addtop("b")
queue1.addtop("c")
print(queue1.size())
print(queue1.removefromq())






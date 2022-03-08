class Array:
    def __init__(self, capacity):
        # [None, None, None, None]
        self.array = [None] * capacity
        self.size = 0

    def insert(self, index, element):
        if index < 0 or index > self.size:
            raise Exception("超出数组实际范围！")
        for i in range(self.size-1, index, -1):
            self.array[i+1] = self.array[i]
        self.array[index] = element
        self.size += 1

    def output(self):
        for i in range(self.size):
            print(self.array[i])

    def remove(self, index):
        if index < 0 or index > self.size:
            raise Exception("超出数组实际范围！")
        for i in range(index, self.size-1):
            self.array[i] = self.array[i+1]
        self.size -= 1


array = Array(6)
array.insert(0, 2)
array.insert(1, 4)
array.insert(2, 6)
array.insert(3, 8)
array.insert(4, 10)
array.insert(5, 12)
array.output()

array.remove(3)
array.output()

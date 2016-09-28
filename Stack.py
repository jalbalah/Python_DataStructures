class Stack:
    def __init__(self):
        self.items = []
        self.size = 0
    def push(self, elem):
        self.items.append(elem)
        self.size += 1
    def pop(self):
        self.size -= 1
        return self.items.pop()
    def peek(self):
        return self.items[-1]
    def isEmpty(self):
        return self.size == 0
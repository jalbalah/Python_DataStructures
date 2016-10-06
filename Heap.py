from heapq import *
class Heap:
    def __init__(self):
        self.heap = []
    def pop(self):
        return heappop(self.heap)
    def push(self, data, priority):
        heappush(self.heap, (priority, data))
    def getParent(self, index):
        return self.heap[int( (index - 1) / 2 )]
    def getLeft(self, index):
        return self.heap[int(2 * index + 1)]
    def getRight(self, index):
        return self.heap[int(2 * index + 2)]
    def __repr__(self):
        return str(self.heap)

heap = Heap()
heap.push("error", 1)
heap.push("debug", 3)
heap.push("warn", 2)
print("heap: " + str(heap))
print("left of root: " + str(heap.getLeft(0)))
print("pop: " + str(heap.pop()))
print("pop: " + str(heap.pop()))
print("pop: " + str(heap.pop()))




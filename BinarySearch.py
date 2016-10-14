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

A = [0, 1, 2, 3, 4, 5, 6]
B = [0, 1, 2, 4, 22, 99, 1004]

def binarySearch(A, x, start=0, end=len(A)-1):
    stack = Stack()
    stack.push( (start, end) )
    while not stack.isEmpty():
        start = stack.pop()
        end = start[1]
        start = start[0]
        if start > end:
            return -1
        mid = int( (start + end) / 2)
        v = A[mid]
        if v > x:
            stack.push( (start, mid - 1) )
            #return binarySearch(A, x, start, mid - 1)
        elif v < x:
            stack.push( (mid + 1, end) )
            #return binarySearch(A, x, mid + 1, end)
    return mid

def r_binarySearch(A, x, start=0, end=len(A)-1):
    if start > end:
        return -1
    mid = int( (start + end) / 2)
    v = A[mid]
    if v > x:
        return binarySearch(A, x, start, mid - 1)
    elif v < x:
        return binarySearch(A, x, mid + 1, end)
    return mid

print("1)", "'" + str(binarySearch(A, 6)) + "'" == "'6'")
print("2)", "'" + str(binarySearch(A, 7)) + "'" == "'-1'")

print("3)", "'" + str(binarySearch(B, 22)) + "'" == "'4'")

print("4)", "'" + str(r_binarySearch(B, 22)) + "'" == "'4'")

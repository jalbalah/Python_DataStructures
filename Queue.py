# from queue import *
# q = Queue()

class Node:
    def __init__(self, value=None, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev
    def __repr__(self):
        return str(self.value)

class Queue:
    def __init__(self):
        self.back = None
        self.front = None
    def enqueue(self, elem):
        # q.put(elem)
        if(self.back == None):  #q.empty()
            self.front = Node(elem) 
            self.back = self.front
        else:
            n = self.back
            self.back = Node(elem, n)
            n.prev = self.back
    def dequeue(self):
        # q.get()
        n = self.front
        if n.prev != None:
            self.front = self.front.prev
            self.front.next = None
        else:
            self.front = None
            self.back = self.front
        return n
    def peek(self):
        return self.front
    def __repr__(self):
        p = self.back
        s = ""
        while p != None:
            s += str(p)+"->"
            p = p.next
        return s

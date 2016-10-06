class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    # O(1)
    def insert(self, data):
        n = Node(data)
        if self.head == None:
            self.head = n
            self.tail = n
        else:
            n.prev = self.tail
            self.tail.next = n
            self.tail = n
    # O(n)
    def contains(self, data):
        n = self.head
        while (n != None) and (n.data != data):
            n = n.next
        if n == None:
            return False
        return True
    # O(n)
    def remov(self, data):
        if self.head == None:
            # len. 0 list
            return False
        n = self.head
        if n.data == data:
            if self.head == self.tail:
                # len. 1 list
                self.head = None
                self.tail = None
            else:
                # remove head
                self.head = self.head.next
                head.prev = None
            return True
        while n.next != None and n.next.data != data:
            n = n.next
        if n.next != None:
            if n.next == self.tail:
                # remove tail
                self.tail = n
            # remove node
            n.next = n.next.next
            return True
        # not found
        return False
    def remove(self, data):
        if self.head == None:
            # len. 0 list
            return False
        if self.head.data == data:
            if self.head == self.tail:
                # len. 1 list
                self.head = None
                self.tail = None
            else:
                # remove head
                self.head = self.head.next
                self.head.prev = None
            return True
        n = self.head.next
        while n != None and n.data != data:
            n = n.next
        if n == self.tail:
            self.tail = self.tail.prev
            self.tail.next = None
            return True
        elif n != None:
            n.prev.next = n.next
            n.next.prev = n.prev
            return True
        # not found
        return False
    def printReverse(self):
        s = ""
        n = self.tail
        while n != None:
            if n == self.head:
                s += str(n)
            else:
                s += str(n) + " <-- "
            n = n.prev
        s = "NULL <-- " + s
        return s
    def __repr__(self):
        s = ""
        head = self.head
        if head == None:
            s += "NULL"
        elif head != None:
            s += str(head)
            head = head.next
            if head == None:
                s += " --> NULL"
        while head != None:
            s += " --> " + str(head)
            head = head.next
            if head == None:
                s += " --> NULL"
        return s
        
class Node:
    def __init__(self, data, next=None, prev=None):
        self.next = None
        self.prev = None
        self.data = data
    def __repr__(self):
        return str(self.data)

ll = LinkedList()
ll.insert(0)
ll.insert(1)
ll.insert(2)
print("print: "+str(ll))
print("print reversed: " + str(ll.printReverse()))
print("contains 1: " + str(ll.contains(1)))
print("remove 1: " + str(ll.remove(1)))
print("print: "+str(ll))

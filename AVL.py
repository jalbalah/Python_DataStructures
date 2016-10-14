import queue
import math

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

class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
    def __repr__(self):
        return "({0})".format(self.data)

class AVLTree:
    def __init__(self):
        self.root = None
        self.count = 0
        
    def find(self, data):
        print("finding... ",data)
        temp = self.root
        while temp != None and temp.data != data:
            if data < temp.data:
                temp = temp.left
            else:
                temp = temp.right
        return temp

    def getMin(self):
        root = self.root
        paren = root
        while root.left != None:
            paren = root
            root = root.left
        return (root, paren)
    # helper function for deleting (pop)
    def delMin(self, rootAndParen):
        root = rootAndParen[0]
        paren = rootAndParen[1]
        self.delete(root.data, root, paren)

    def delete(self, data, n = False, paren = False):
        print("deleting... ",data)
        self.count -= 1
        if n == False:
            # calling delete from root... find node
            temp = self.root
            paren = temp
            while temp != None and temp.data != data:
                paren = temp
                if data < temp.data:
                    temp = temp.left
                else:
                    temp = temp.right
            n = temp
        if n == None:
            print(str(data)+" not found.")
        else:
            # leaf
            if n.left == None and n.right == None:
                if n == self.root:
                    self.root= None
                elif n.data < paren.data:
                    paren.left = None
                else:
                    paren.right = None
            # left subtree only
            elif n.left != None and n.right == None:
                if n == self.root:
                    # root quirk (no obj. refs. in python)
                    if n.data <= paren.data:
                        self.root = self.root.left
                    else:
                        self.root = self.root.left
                elif n.data <= paren.data:
                    paren.left = n.left
                else:
                    paren.right = n.left
            # right subtree only
            elif n.left == None and n.right != None:
                if n == self.root:
                    # root quirk (no obj. refs. in python)
                    if n.data <= paren.data:
                        self.root = self.root.right
                    else:
                        self.root = self.root.right
                if n.data < paren.data:
                    paren.left = n.right
                else:
                    paren.right = n.right
            # right and left subtrees
            else:
                mn = n.right
                paren = mn
                while mn.left != None:
                    paren = mn
                    mn = mn.left  # min in right subtree
                n.data = mn.data
                if n == self.root:
                    paren = self.root
                self.delete(mn.data, mn, paren) # recurs. min subtree
            
            self.__balanceTree(paren)
        
    def insert(self, data):
        self.count += 1
        if self.root == None:
            self.root = Node(data)
        else:
            temp = self.root
            greatGrand = temp
            grandParen = temp
            paren = temp
            while temp != None:
                greatGrand = grandParen
                grandParen = paren
                paren = temp
                if data < temp.data:
                    temp = temp.left
                else:
                    temp = temp.right
            if paren.data == data:
                pass
            else:
                if data < paren.data:
                    paren.left = Node(data)
                    temp = paren.left
                else:
                    paren.right = Node(data)
                    temp = paren.right
                                    
                self.__reBalanceTree(grandParen.data)       
        
    def __reBalanceTree(self, data):
        root = self.root
        nodes = []
        while root.data != data:
            nodes.append(root)
            if data < root.data:
                root = root.left
            else:
                root = root.right
        nodes.append(root)
        c = len(nodes) - 1
        while (c >= 0) and (not self.__balanceTree(nodes[c])):
            c -= 1

    def __balanceTree(self, grandParen):
        bfGP = self.__balanceFactor(grandParen)
        if bfGP == 2:
            bfP = self.__balanceFactor(grandParen.left)
            if bfP == -1:
                self.__leftRight(grandParen.left.right, grandParen.left)
            self.__leftLeft(grandParen.left, grandParen)
            return True
        elif bfGP == -2:
            bfP = self.__balanceFactor(grandParen.right)
            if bfP == 1:
                self.__rightLeft(grandParen.right.left, grandParen.right)
            self.__rightRight(grandParen.right, grandParen)
            return True
        return False            

    def __rightLeft(self, temp, paren):
        data = paren.data
        C = temp.right       
        D = paren.right
        B = paren.left.left
        paren.data = temp.data
        paren.right = Node(data)
        paren.right.right = D
        paren.right.left = C
        paren.left = B
    
    def __rightRight(self, paren, grandParen):
        data = grandParen.data
        A = grandParen.left
        B = paren.left        
        grandParen.data = paren.data
        grandParen.right = paren.right
        grandParen.left = Node(data)  # duplicate the node...
        # note: no pointers / dereferencing in python without ctype
        grandParen.left.left = A
        grandParen.left.right = B

    def __leftRight(self, temp, paren):
        data = paren.data
        A = paren.left
        B = temp.left
        C = temp.right
        paren.data = temp.data
        paren.left = Node(data)
        paren.left.left = A
        paren.left.right = B
        paren.right = C
    
    def __leftLeft(self, paren, grandParen):
        data = grandParen.data
        D = grandParen.right
        C = paren.right
        grandParen.data = paren.data
        grandParen.left = paren.left
        grandParen.right = Node(data)  # duplicate the node...
        # note: no pointers / dereferencing in python without ctype
        grandParen.right.left = C
        grandParen.right.right = D
        
    def __balanceFactor(self, node):
        if node.left == None:
            heightLeft = -1
        else:
            heightLeft = self.__getHeight(node.left)
        if node.right == None:
            heightRight = -1
        else:
            heightRight = self.__getHeight(node.right)
        return heightLeft - heightRight

    def __getHeight(self, node):
        if node == None:
            return -1
        q = queue.Queue()
        mxDepth = 0
        q.put((node, mxDepth))
        while not q.empty():
            n = q.get()
            depth = n[1]
            mxDepth = max(depth, mxDepth)
            n = n[0]
            if n.left != None:
                q.put((n.left, depth + 1))
            if n.right != None:
                q.put((n.right, depth + 1))
        return mxDepth
    
    def __repr__(self):
        s = ""
        q = queue.Queue()
        level = 1
        tree = []
        q.put((self.root, level))
        spacer = " " * 6
        c = 1
        levelSize = 1
        lastLevel = 1
        while not q.empty():
            n = q.get()
            tree.append([])
            level = n[1]
            n = n[0]
            if n!= None and not type(n) is str:
                #s += str(n)
                if n.left != None:
                    q.put((n.left, level + 1))
                if n.right != None:
                    q.put((n.right, level + 1))
            tree[c - 1] += str(n)
            level = math.log(c + 1) / math.log(2)
            if int(level) == level:
                levelSize = int( (pow(2,level)-1) - (pow(2,level-1)-1) )
                tree[c - 1] += ("\n" + (" / \\ " * (levelSize)) + "\n")
            c += 1
        for level in range(0, len(tree)):
            s += "".join(tree[level])
        return s  # str(tree)
    
    def inOrder(self):
        stack = Stack()
        root = self.root
        s = ""
        while not stack.isEmpty() or root != None:
            if root != None:
                stack.push(root)
                root = root.left
            else:
                root = stack.pop()
                s += str(root) + " "
                root = root.right        
        print("in order: " + s)

    def popMin(self):
        pass

avl = AVLTree()
for x in range(1,11):
    avl.insert(x)
for x in range(1,11):
    n = avl.getMin()
    print(n)
    avl.delMin(n)
#avl.insert(.5)
#avl.insert(1)
#avl.insert(0)
#avl.insert(1.5)
#print("--\n"+str(avl))
#avl.delete(0)
#print(str(avl))
avl.inOrder()
print(avl)
                
        

# Depth first search

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

class TreeNode:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    def __repr__(self):
        return str(self.value)

# recursive also uses a [call] stack...

def preOrder(root):
    s = ""
    stack = Stack()
    stack.push(root)
    while not stack.isEmpty():
        n = stack.pop()
        s += str(n) + " "
        if(n != None):
            if(n.right != None):
                stack.push(n.right)
            if(n.left != None):
                stack.push(n.left)
    return s
def r_preOrder(root):
    s = ""
    if root != None:
        s += str(root) + " "
        s += r_preOrder(root.left)
        s += r_preOrder(root.right)
    return s

def inOrder(root):
    s = ""
    stack = Stack()
    while not stack.isEmpty() or root != None:
        if root != None:
            stack.push(root)
            root = root.left
        else:
            root = stack.pop()
            s += str(root) + " "
            root = root.right
    return s
def r_inOrder(root):
    s = ""
    if root != None:
        s += r_inOrder(root.left)
        s += str(root) + " "
        s += r_inOrder(root.right)
    return s

def postOrder(root):
    s = ""
    stack = Stack()
    last = None
    while not stack.isEmpty() or root != None:
        if root != None:
            stack.push(root)
            root = root.left
        else:
            peek = stack.peek()
            if peek.right != None and last != peek.right:
                root = peek.right
            else:
                s += str(peek) + " "
                last = stack.pop()
    return s
def r_postOrder(root):
    s = ""
    if root != None:
        s += r_postOrder(root.left)
        s += r_postOrder(root.right)
        s += str(root) + " "
    return s

root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right = TreeNode(3)
print("""Example Binary Search Tree:
Level 1:        1    \n
              /   \  \n
Level 2:     2     3 \n
            / \      \n
Level 3:   4   5     \n
""")

# 1 2 4 5 3 ...
print("Pre-Order iterative:",preOrder(root))
print("Pre-Order recursive:",r_preOrder(root),"\n")

# 4 2 5 1 3 ...
print("In-Order iterative:",inOrder(root))
print("In-Order recursive:",r_inOrder(root),"\n")

# 4 5 2 3 1 ...
print("Post-Order iterative:",postOrder(root))
print("Post-Order recursive:",r_postOrder(root),"\n")


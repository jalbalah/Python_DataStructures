import queue

class TreeNode:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    def __repr__(self):
        return str(self.value)
    
root = TreeNode(3)
root.left = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(4)
root.right = TreeNode(2)
root.right.left = TreeNode(6)
print("""
Level 1:        3    \n
              /   \  \n
Level 2:     5     2 \n
            / \    / \n
Level 3:   1   4  6  \n
""")

# 3 5 2 1 4 6
# use a stack
def levelOrder(root):
    s = ""
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        n = q.get()
        s += str(n) + " "
        if(n != None):
            if(n.left != None):
                q.put(n.left)
            if(n.right != None):
                q.put(n.right)
    return s

print(levelOrder(root))

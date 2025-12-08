class Node:
    def __init__(self,root):
        self.data=root
        self.left=None
        self.right=None

def trav(node):
    if node is None:
        return 
    trav(node.left)
    print(str(node.data))
    trav(node.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)
print("InOrder traversal")
trav(root)
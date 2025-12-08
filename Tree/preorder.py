class Node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None

def trav(node):
    if node is None:
        return
    print(node.data)
    trav(node.left)
    trav(node.right)
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)
print("PreOrder traversal")
trav(root)
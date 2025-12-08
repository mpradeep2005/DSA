class Node:
    def __init__(self,data):
        self.data=data
        self.left =None
        self.right=None

def trav(node):
    if node is None:
        return
    trav(node.left)
    trav(node.right)
    print(node.data)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)
print("PostOrder traversal")
trav(root)
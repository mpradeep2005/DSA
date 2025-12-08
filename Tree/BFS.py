class Node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None

def trav(node):
    q=[node]

    while q:
        node=q.pop(0)
        print(node.data)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
            
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)
print("BFS traversal")
trav(root)
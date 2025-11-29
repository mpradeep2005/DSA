class single_node:
    def __init__(self,value,next=None):
        self.value=value
        self.next=next
    
    def __str__(self):
        return str(self.value)

def link_rec(node):
    if node is None:
        print()
        return
    print(node)
    link_rec(node.next) 

head=single_node(10)
a=single_node(20)
b=single_node(30)
c=single_node(40)

head.next=a
a.next=b
b.next=c

link_rec(head)
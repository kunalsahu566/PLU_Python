class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def leaf(root):
    if root:
        if root.left is None and root.right is None:
            print(root.data)
        leaf(root.left)
        leaf(root.right)

root = Node(50)
root.left = Node(30)
root.right = Node(70)

print("Leaf Nodes:")
leaf(root)
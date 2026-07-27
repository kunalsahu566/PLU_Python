class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def count(root):
    if root is None:
        return 0
    return 1 + count(root.left) + count(root.right)

root = Node(50)
root.left = Node(30)
root.right = Node(70)

print("Total Nodes:", count(root))
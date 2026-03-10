class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = Node(10)

print("Root Tree:", root.data)
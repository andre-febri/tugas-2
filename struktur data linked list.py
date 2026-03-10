class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# membuat node
n1 = Node(10)
n2 = Node(20)

# menghubungkan node
n1.next = n2

# menampilkan data
print(n1.data, "->", n1.next.data)
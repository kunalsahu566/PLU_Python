class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)


temp = head
while temp:
    if temp.data == 20:
        new_node = Node(25)
        new_node.next = temp.next
        temp.next = new_node
        break
    temp = temp.next


temp = head
while temp:
    print(temp.data, end=" ")
    temp = temp.next
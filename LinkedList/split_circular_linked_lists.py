class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = self.tail = None
        self.length = 0

    def is_empty(self):
        return self.length == 0

    def push(self, x):
        node = Node(x)
        if self.is_empty():
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.length += 1
        self.tail.next = self.head

    def show(self):
        curr = self.head
        while curr and curr.next is not self.head:
            print(curr.data, end=" ")
            curr = curr.next
        print(curr.data, end=" ")
        print()


l = LinkedList()
for i in [1, 2, 3, 4]:
    l.push(i)
l.show()

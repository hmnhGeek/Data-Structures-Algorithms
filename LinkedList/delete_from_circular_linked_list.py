class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
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
        self.tail.next = self.head
        self.length += 1

    def show(self):
        curr = self.head
        while curr.next != self.head:
            print(curr.data, end=" ")
            curr = curr.next
        print(curr.data, end=" ")
        print()


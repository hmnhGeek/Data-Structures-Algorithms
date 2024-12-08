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

    def delete(self, index):
        if self.is_empty():
            return
        if index not in range(self.length):
            return
        curr = self.head
        counter = 0
        prev = self.tail
        while counter != index:
            prev = curr
            curr = curr.next
            counter += 1
        prev.next = curr.next
        if curr == self.head:
            self.head = curr.next
        elif curr == self.tail:
            self.tail = prev
        self.length -= 1


cll = CircularLinkedList()
for i in [2, 6, 8, 0, 9, 9, 7]:
    cll.push(i)
cll.show()
cll.delete(0)
cll.show()
cll.delete(5)
cll.show()
cll.delete(2)
cll.show()

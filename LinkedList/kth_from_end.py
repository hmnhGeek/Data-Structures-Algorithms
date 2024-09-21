class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = self.tail = None
        self.length = 0

    def build(self, arr):
        for i in arr:
            self.push(i)

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

    def get(self, index):
        if index < 0 or index >= self.length:
            return Node(-1)
        counter = 1
        curr = self.head
        while counter != index + 1:
            curr = curr.next
            counter += 1
        return curr

    def get_from_end(self, k):
        return self.get(self.length - k)


l = LinkedList()
l.build([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(l.get_from_end(2).data)

l = LinkedList()
l.build([10, 5, 100, 5])
print(l.get_from_end(5).data)
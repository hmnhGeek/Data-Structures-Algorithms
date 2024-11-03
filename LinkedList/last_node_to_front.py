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

    def move_to_front(self):
        if self.is_empty():
            return
        if self.length == 1:
            return

        prev, curr = None, self.head
        while curr != self.tail:
            prev = curr
            curr = curr.next

        if prev is not None:
            prev.next = None
        if curr is not None:
            curr.next = self.head
            self.head = curr

    def show(self):
        curr = self.head
        while curr is not None:
            print(curr.data, end=" ")
            curr = curr.next
        print()

    def build(self, _list):
        for i in _list:
            self.push(i)


# Example 1
l = LinkedList()
l.build([2, 5, 6, 2, 1])
l.show()
l.move_to_front()
l.show()


# Example 2
l = LinkedList()
l.build([1, 2, 3, 4, 5])
l.show()
l.move_to_front()
l.show()
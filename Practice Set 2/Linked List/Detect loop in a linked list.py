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

    def build(self, *args):
        for i in args:
            self.push(i)

    def show(self):
        curr = self.head
        while curr is not None:
            print(curr.data, end=" ")
            curr = curr.next
        print()

    def pop(self):
        if self.is_empty():
            return
        item = self.head.data
        node = self.head
        self.head = self.head.next
        del node
        self.length -= 1
        return item

    def has_loop(self):
        slow, fast = self.head, self.head.next
        while slow and fast and fast.next:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next
        return False


# Example 1
l = LinkedList()
l.build(1, 3, 4)
l.show()
print(l.has_loop())
l.tail.next = l.head.next
print(l.has_loop())
print()

# Example 2
l = LinkedList()
l.build(1, 8, 3, 4)
l.show()
print(l.has_loop())
print()

# Example 3
l = LinkedList()
l.build(1, 2, 3, 4)
l.show()
print(l.has_loop())
l.tail.next = l.head
print(l.has_loop())
print()

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
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

    def pop(self):
        if self.is_empty():
            return
        item = self.head.data
        node = self.head
        self.head = self.head.next
        del node
        self.length -= 1
        return item

    def show(self):
        curr = self.head
        while curr is not None:
            print(curr.data, end=" ")
            curr = curr.next
        print()

    def _reverse(self, prev, curr):
        if curr is None:
            return
        next_curr = curr.next
        curr.next = prev
        prev = curr
        curr = next_curr
        self._reverse(prev, curr)

    def reverse(self):
        self._reverse(None, self.head)
        self.head, self.tail = self.tail, self.head


def test(*args):
    q = Queue()
    for i in args:
        q.push(i)
    q.show()
    q.reverse()
    q.show()
    print()


test(4, 3, 1, 10, 2, 6)
test(4, 3, 2, 1)
test(7, 9, 5, 12, 8)
test(1)
test()
test(2, 8)
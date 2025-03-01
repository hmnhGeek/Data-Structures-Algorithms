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

    def show(self):
        curr = self.head
        while curr is not None:
            print(curr.data, end=" ")
            curr = curr.next
        print()

    def iterative_reverse(self):
        prev, curr = None, self.head
        while curr is not None:
            next_curr = curr.next
            curr.next = prev
            prev = curr
            curr = next_curr
        self.head, self.tail = self.tail, self.head

    def _reverse(self, prev, curr):
        if curr is None:
            self.head, self.tail = self.tail, self.head
            return
        next_curr = curr.next
        curr.next = prev
        prev = curr
        curr = next_curr
        return self._reverse(prev, curr)

    def recursive_reverse(self):
        self._reverse(None, self.head)


l = LinkedList()
for i in [1,2,4,8,9,6]:
    l.push(i)
l.show()
l.iterative_reverse()
l.show()
l.recursive_reverse()
l.show()

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
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
            node.next = self.head
            self.head = node
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

    def __str__(self):
        if self.is_empty():
            return "[]"
        result = "["
        curr = self.head
        while curr != self.tail:
            result += f"{curr.data}, "
            curr = curr.next
        result += f"{self.tail.data}]"
        return result

    def reverse(self):
        self._reverse(None, self.head)
        self.head, self.tail = self.tail, self.head

    def _reverse(self, prev, curr):
        if curr is None:
            return
        next_curr = curr.next
        curr.next = prev
        prev = curr
        curr = next_curr
        self._reverse(prev, curr)


s1 = Stack()
for i in [1, 2, 3, 4]:
    s1.push(i)
print(s1)
s1.reverse()
print(s1)

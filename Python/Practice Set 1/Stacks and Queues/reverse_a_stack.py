# Problem link - https://www.geeksforgeeks.org/reverse-a-stack-using-recursion/


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

    def _reverse(self, prev, curr):
        if curr is None:
            return
        next_curr = curr.next
        curr.next = prev
        return self._reverse(curr, next_curr)

    def reverse(self):
        # The recursion will run for all the nodes in one go, and hence time and space complexities both are O(n).
        self._reverse(None, self.head)
        # once reversed, ensure to swap head and tail pointers.
        self.head, self.tail = self.tail, self.head


s1 = Stack()
for i in [1, 2, 3, 4]:
    s1.push(i)
s1.reverse()
while not s1.is_empty():
    print(s1.pop(), end=" ")
print()
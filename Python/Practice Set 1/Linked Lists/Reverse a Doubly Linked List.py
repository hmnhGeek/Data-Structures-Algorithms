# Problem link - https://www.geeksforgeeks.org/problems/reverse-a-doubly-linked-list/1


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = self.tail = None
        self.length = 0

    def is_empty(self):
        return self.length == 0

    def build(self, *args):
        for i in args:
            self.push(i)

    def push(self, x):
        node = Node(x)
        if self.is_empty():
            self.head = self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.length += 1

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
        """
            Time complexity is O(n) and space complexity is O(1).
        """
        if self.is_empty() or self.length == 1:
            return
        prev, curr = None, self.head
        while curr is not None:
            next_curr = curr.next
            curr.next = prev
            curr.prev = next_curr
            prev = curr
            curr = next_curr
        self.head, self.tail = self.tail, self.head


dll = DoublyLinkedList()
dll.build(3, 4, 5)
print(dll)
dll.reverse()
print(dll)

print()

dll = DoublyLinkedList()
dll.build(75, 122, 59, 196)
print(dll)
dll.reverse()
print(dll)

print()

dll = DoublyLinkedList()
dll.build(1)
print(dll)
dll.reverse()
print(dll)

print()

dll = DoublyLinkedList()
dll.build()
print(dll)
dll.reverse()
print(dll)

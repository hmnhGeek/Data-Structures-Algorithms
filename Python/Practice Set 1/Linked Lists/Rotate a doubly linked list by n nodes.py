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

    def push(self, x):
        node = Node(x)
        if self.is_empty():
            self.head = self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.length += 1

    def build(self, *args):
        for i in args:
            self.push(i)

    def __str__(self):
        if self.is_empty():
            return "[]"
        curr = self.head
        result = "["
        while curr != self.tail:
            result += f"{curr.data}, "
            curr = curr.next
        result += f"{self.tail.data}]"
        return result

    def rotate(self, p):
        if p < 0 or p >= self.length:
            return
        curr = self.head
        counter = 1
        while counter != p:
            curr = curr.next
            counter += 1
        next_node = curr.next
        next_node.prev = None
        self.tail.next = self.head
        self.head.prev = self.tail
        curr.next = None
        self.head = next_node
        self.tail = curr


class Solution:
    @staticmethod
    def test(p, *args):
        dll = DoublyLinkedList()
        dll.build(*args)
        print(dll)
        dll.rotate(p)
        print(dll)


Solution.test(2, 1, 2, 3, 4, 5)
Solution.test(3, 2, 6, 5, 4)

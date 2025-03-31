# Problem link - https://www.geeksforgeeks.org/problems/reverse-a-doubly-linked-list/1


class Node:
    def __init__(self, data):
        self.prev = self.next = None
        self.data = data


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

    def show(self):
        curr = self.head
        while curr is not None:
            print(curr.data, end=" ")
            curr = curr.next
        print()

    def reverse(self):
        """
            Time complexity is O(n) and space complexity is O(1).
        """
        prev, curr = None, self.head
        while curr is not None:
            next_curr = curr.next
            curr.next = prev
            # additional step of handling the prev pointer
            curr.prev = next_curr
            prev = curr
            curr = next_curr
        self.head, self.tail = self.tail, self.head


def test(*args):
    dll = DoublyLinkedList()
    dll.build(*args)
    print("Before reversing")
    dll.show()
    dll.reverse()
    print("After reversing")
    dll.show()
    print()


test(3, 4, 5)
test(75, 122, 59, 196)
test(1, 2, 3)
test(1)
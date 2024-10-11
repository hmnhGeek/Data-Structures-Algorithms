# Problem link - https://www.geeksforgeeks.org/reverse-a-linked-list/


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = self.tail = None
        self.length = 0

    def build(self, l):
        for i in l:
            self.push(i)

    def push(self, x):
        node = Node(x)
        if self.length == 0:
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

    def reverse(self):
        prev, curr = None, self.head
        while curr is not None:
            next_curr = curr.next
            curr.next = prev
            prev = curr
            curr = next_curr
        self.head, self.tail = self.tail, self.head

    def recursive_reverse(self, prev, curr):
        if prev is None:
            self.tail = curr
        if curr is None:
            self.head = prev
            return prev
        next_curr = curr.next
        curr.next = prev
        return self.recursive_reverse(curr, next_curr)


def test_iterative(l):
    print("\nTesting iterative reverse method.")
    linked_list = LinkedList()
    linked_list.build(l)
    print("Original List:")
    linked_list.show()
    linked_list.reverse()
    print("Reversed List:")
    linked_list.show()


def test_recursive(l):
    print("\nTesting recursive reverse method.")
    linked_list = LinkedList()
    linked_list.build(l)
    print("Original List:")
    linked_list.show()
    linked_list.recursive_reverse(None, linked_list.head)
    print("Reversed List:")
    linked_list.show()


test_iterative([1, 2, 3, 4, 5])
test_recursive([1, 2, 3, 4, 5])
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = self.tail = None

    def push(self, x):
        node = Node(x)

        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def reverse(self):
        curr = self.head
        prev = None
        while curr is not None:
            next_curr = curr.next
            curr.next = prev
            prev = curr
            curr = next_curr
        self.head, self.tail = self.tail, self.head

    def flatten(self):
        self.reverse()
        max_node = float('-inf')
        prev, curr = None, self.head
        while curr is not None:
            if curr.data < max_node:
                if prev is not None:
                    prev.next = curr.next
                if curr == self.tail:
                    self.tail = prev
                curr = curr.next
            elif max_node < curr.data:
                max_node = curr.data
                prev = curr
                curr = curr.next
            else:
                prev = curr
                curr = curr.next
        self.reverse()

    def show(self):
        curr = self.head
        while curr is not None:
            print(curr.data, end=" ")
            curr = curr.next
        print()


def test(example_list):
    l = LinkedList()
    for i in example_list:
        l.push(i)
    l.show()
    l.flatten()
    l.show()
    print()


test([12, 15, 10, 11, 5, 6, 2, 3])

test([10, 20, 30, 40, 50, 60])

test([8, 7, 8, 4, 5, 6, 2, 1, -1])

test([6, 5, 3, 2, 1, -1])

test([10, 8, 7, 12, 5, -1])

test([5, 6, 7, 8, 10, 12, -1])
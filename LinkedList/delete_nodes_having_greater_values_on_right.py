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


l = LinkedList()
for i in [12, 15, 10, 11, 5, 6, 2, 3]:
    l.push(i)
l.show()
l.flatten()
l.show()


l1 = LinkedList()
for i in [10, 20, 30, 40, 50, 60]:
    l1.push(i)
l1.show()
l1.flatten()
l1.show()


l2 = LinkedList()
for i in [8, 7, 8, 4, 5, 6, 2, 1, -1]:
    l2.push(i)
l2.show()
l2.flatten()
l2.show()


l3 = LinkedList()
for i in [6, 5, 3, 2, 1, -1]:
    l3.push(i)
l3.show()
l3.flatten()
l3.show()


l4 = LinkedList()
for i in [10, 8, 7, 12, 5, -1]:
    l4.push(i)
l4.show()
l4.flatten()
l4.show()


l5 = LinkedList()
for i in [5, 6, 7, 8, 10, 12, -1]:
    l5.push(i)
l5.show()
l5.flatten()
l5.show()
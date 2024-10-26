# Problem link - https://www.geeksforgeeks.org/problems/remove-loop-in-linked-list/1


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = self.tail = None
        self.length = 0

    def push(self, x):
        node = Node(x)
        if self.length == 0:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.length += 1

    def build(self, l):
        for i in l:
            self.push(i)

    def delete_loop(self):
        self.tail.next = None

    def show(self):
        if self.tail.next is not None:
            print("Loop detected!")
            return
        curr = self.head
        while curr is not None:
            print(curr.data, end=" ")
            curr = curr.next
        print()


l = LinkedList()
l.build([1, 2, 3, 4, 5])
l.tail.next = l.head.next.next
l.show()
l.delete_loop()
l.show()
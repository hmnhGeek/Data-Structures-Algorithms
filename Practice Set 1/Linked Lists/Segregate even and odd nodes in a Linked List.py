# Problem link - https://www.geeksforgeeks.org/problems/segregate-even-and-odd-nodes-in-a-linked-list5035/1


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

    def segregate(self):
        """
            Time complexity is O(n) and space complexity is O(n).
        """

        odd = ot = Node(None)
        even = ev = Node(None)
        curr = self.head
        while curr is not None:
            if curr.data % 2 == 0:
                ev.next = curr
                ev = curr
            else:
                ot.next = curr
                ot = curr
            curr = curr.next
        ev.next = odd.next
        self.head = even.next
        self.tail = ot
        ot.next = None


l = LinkedList()
for i in [17, 15, 8, 9, 2, 4, 6]:
    l.push(i)
l.show()
l.segregate()
l.show()

print()
l = LinkedList()
for i in [1, 3, 5, 7]:
    l.push(i)
l.show()
l.segregate()
l.show()

print()
l = LinkedList()
for i in [2,1,4,8,6,8,93,94,0]:
    l.push(i)
l.show()
l.segregate()
l.show()

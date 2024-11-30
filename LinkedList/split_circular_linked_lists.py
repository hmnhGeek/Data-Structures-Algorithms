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
        self.tail.next = self.head

    def show(self):
        curr = self.head
        while curr and curr.next is not self.head:
            print(curr.data, end=" ")
            curr = curr.next
        print(curr.data, end=" ")
        print()

    def split(self):
        if self.length <= 1:
            return
        slow, fast = self.head, self.head.next
        self.tail.next = None
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # slow is now at the middle node.
        next_list_head = slow.next

        slow.next = self.head
        l1 = LinkedList()
        l1.head = self.head
        l1.tail = slow

        l2 = LinkedList()
        l2.head = next_list_head
        l2.tail = self.tail
        self.tail.next = next_list_head

        return l1, l2


def test(*args):
    l = LinkedList()
    for i in args:
        l.push(i)
    l.show()
    l1, l2 = l.split()
    l1.show()
    l2.show()
    print()


test(10, 4, 9)
test(10, 4, 9, 10)
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = self.tail = None

    def _push(self, x):
        node = Node(x)
        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def build(self, *args):
        for i in args:
            self._push(i)

    def show(self):
        curr = self.head
        while curr is not None:
            print(curr.data, end=" ")
            curr = curr.next
        print()

    def reverse(self):
        prev = None
        curr = self.head
        while curr is not None:
            next_curr = curr.next
            curr.next = prev
            prev = curr
            curr = next_curr
        self.head, self.tail = self.tail, self.head

    def get_middle_node(self):
        slow = self.head
        fast = slow.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def is_palindrome(self):
        middle_node = self.get_middle_node()
        next_head = middle_node.next
        middle_node.next = None
        l1 = LinkedList()
        l1.head = self.head
        l1.tail = middle_node
        l2 = LinkedList()
        l2.head = next_head
        l2.tail = self.tail
        l2.reverse()
        curr1, curr2 = l1.head, l2.head
        palindrome = True
        while curr2 is not None:
            if curr1.data != curr2.data:
                palindrome = False
            curr1 = curr1.next
            curr2 = curr2.next
        l2.reverse()
        l1.tail.next = l2.head
        return palindrome


def test(*args):
    l = LinkedList()
    l.build(*args)
    l.show()
    print(l.is_palindrome())
    l.show()
    print()


test(1, 2, 2, 1)
test(1, 2, 3, 4)
test(1, 2, 3, 2, 1)
test(1, 2, 3, 4, 1)
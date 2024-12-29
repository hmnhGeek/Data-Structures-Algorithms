# Problem link - https://www.naukri.com/code360/problems/rotate-dll_1115782


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

    def get_length(self):
        return self.length

    def push(self, x):
        node = Node(x)
        if self.is_empty():
            self.head = self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.length += 1

    def show(self):
        curr = self.head
        while curr is not None:
            print(curr.data, end=" ")
            curr = curr.next
        print()

    def rotate(self, p):
        """
            Time complexity is O(p) and space complexity is O(1).
        """

        # if p is out of range, do nothing.
        if p < 0 or p > self.get_length():
            return

        # go to the pth node in O(p) time.
        curr = self.head
        counter = 1
        while counter != p:
            curr = curr.next
            counter += 1

        head, tail = self.head, self.tail

        # make the tail's next point to the current head.
        tail.next = head
        # make the head's prev point to the current tail.
        head.prev = tail

        # also, store the reference to pth node's next as it will become head.
        next_head = curr.next

        # if pth node's next is not None
        if curr.next is not None:
            # ensure that next_head's prev is None as it will become head now.
            curr.next.prev = None
            # and the pth node will become tail, so ensure that its next is None.
            curr.next = None

        # update head and tail of the DLL.
        self.head, self.tail = next_head, curr


def test(*args):
    p = args[-1]
    n = len(args) - 1
    dll = DoublyLinkedList()
    for i in range(n):
        dll.push(args[i])
    dll.show()
    dll.rotate(p)
    dll.show()


test(1, 2, 3, 4, 5, 2)
test(2, 6, 5, 4, 3)
test(4, 3, 9, 1, 7, 8, 4)
test(6, 2, 4, 2, 1, 4, 2)
test(12, 33, 55, 11, 22, 3)

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

    def build(self, _list):
        for i in _list:
            self.push(i)

    def show(self):
        curr = self.head
        while curr is not None:
            print(curr.data, end=" ")
            curr = curr.next
        print()


class LinkedListSplitter:
    def __init__(self, linked_list: LinkedList):
        self.linked_list = linked_list

    def split(self):
        dummy_node = Node(None)
        dummy_node.next = self.linked_list.head
        last_node = None
        prev, curr = None, self.linked_list.head

        while curr is not None:
            if curr != self.linked_list.head and curr.data % 2 == 0:
                next_curr = curr.next
                if prev is not None:
                    prev.next = curr.next
                curr.next = self.linked_list.head
                if last_node is not None:
                    last_node.next = curr
                if dummy_node.next == self.linked_list.head:
                    dummy_node.next = curr
                last_node = curr
                curr = next_curr
            else:
                prev = curr
                curr = curr.next

        self.linked_list.head = dummy_node.next
        self.linked_list.tail = prev


def test(_list):
    l = LinkedList()
    l.build(_list)
    l.show()
    splitter = LinkedListSplitter(l)
    splitter.split()
    l.show()
    print()


test([17, 15, 8, 9, 2, 4, 6])
test([1, 3, 5, 7])
test([17, 15, 8, 12, 10, 5, 4, 1, 7, 6])
test([1, 2, 3, 4, 5])
test([2, 1, 3, 5, 6, 4, 7])
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

    def show(self):
        curr = self.head
        while curr is not None:
            print(curr.data, end=" ")
            curr = curr.next
        print()


class LinkedListSplitter:
    def __init__(self, linked_list: LinkedList):
        self.l = linked_list

    def split(self):
        temp = Node(None)
        original_temp = None
        prev = None
        curr = self.l.head
        while curr is not None:
            if curr.data % 2 == 0:
                if temp.next is None:
                    temp = curr
                    original_temp = temp
                else:
                    temp.next = curr
                    temp = curr
                if prev:
                    prev.next = curr.next
                next_curr = curr.next
                curr.next = self.l.head
                curr = next_curr
            else:
                prev = curr
                curr = curr.next

        if original_temp:
            self.l.head = original_temp


def test(_list):
    l = LinkedList()
    for i in _list:
        l.push(i)
    l.show()
    LinkedListSplitter(l).split()
    l.show()


test([17, 15, 8, 9, 2, 4, 6])
print()
test([1, 3, 5, 7])
print()
test([1, 2, 3, 4, 5, 6])
print()
test([2, 1, 3, 5, 6, 4, 7])

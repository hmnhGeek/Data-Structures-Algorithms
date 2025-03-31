# Problem link - https://www.geeksforgeeks.org/reverse-a-linked-list-in-groups-of-given-size/

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = self.tail = None
        self.length = 0

    def _build(self, l):
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

    def reverse(self):
        prev, curr = None, self.head
        while curr is not None:
            next_curr = curr.next
            curr.next = prev
            prev = curr
            curr = next_curr
        self.head, self.tail = self.tail, self.head

    def show(self):
        curr = self.head
        while curr is not None:
            print(curr.data, end=" ")
            curr = curr.next
        print()

    def _get_kth_node(self, curr, k):
        counter = 1
        prev = None
        while counter != k:
            prev = curr
            curr = curr.next
            if curr is None:
                return prev
            counter += 1
        return curr

    def reverse_in_parts(self, k):
        temp = None
        next_temp = curr = self.head
        while curr is not None:
            kth_node = self._get_kth_node(curr, k)
            next_curr = kth_node.next
            kth_node.next = None

            if temp is not None:
                temp.next = kth_node

            if temp is None:
                self.head = kth_node

            if next_curr is None:
                self.tail = curr

            sub_list = LinkedList()
            sub_list.head = next_temp
            sub_list.tail = kth_node
            sub_list.reverse()

            temp = next_temp
            curr = next_curr
            next_temp = next_curr


def test(_list, k):
    l = LinkedList()
    l._build(_list)
    l.show()
    l.reverse_in_parts(k)
    l.show()
    print()


test([1, 2, 3, 4, 5], 2)
test([1, 2, 3, 4, 5], 3)
test([1, 2, 3, 4, 5, 6], 4)
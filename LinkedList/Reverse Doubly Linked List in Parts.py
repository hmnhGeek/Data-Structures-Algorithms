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

    def reverse(self):
        prev, curr = None, self.head
        while curr is not None:
            next_curr = curr.next
            curr.next = prev
            curr.prev = next_curr
            prev = curr
            curr = next_curr
        self.head, self.tail = self.tail, self.head

    def _get_kth_node(self, prev, start_node, k):
        counter = 1
        prev = None
        while counter != k and start_node is not None:
            prev = start_node
            start_node = start_node.next
            counter += 1
        if start_node is None:
            return prev
        return start_node

    def reverse_in_parts(self, k):
        if k == self.length:
            self.reverse()
        if k <= 0:
            return
        start_node = curr = self.head
        last_node = None
        while curr is not None:
            kth_node = self._get_kth_node(None, curr, k)
            temp = kth_node.next
            kth_node.next = None
            if temp is not None:
                temp.prev = None
            sub_dll = DoublyLinkedList()
            sub_dll.head = start_node
            sub_dll.tail = kth_node
            sub_dll.reverse()

            if last_node is not None:
                last_node.next = kth_node
                kth_node.prev = last_node
            else:
                self.head = kth_node

            if temp is None:
                self.tail = start_node

            last_node = start_node
            curr = start_node = temp


def test(*args):
    k = args[-1]
    n = len(args)
    dll = DoublyLinkedList()
    for i in range(n - 1):
        dll.push(args[i])
    dll.show()
    dll.reverse_in_parts(k)
    dll.show()


test(1, 2, 3, 4, 5, 6, 4)
test(1, 2, 3, 4, 5, 6, 2)
test(1, 2, 3, 4, 5, 2)
test(1, 2, 3, 4, 5, 3)
test(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 3)
test(5, 4, 3, 7, 9, 2, 4)

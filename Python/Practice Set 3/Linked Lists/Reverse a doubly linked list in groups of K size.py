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

    def build(self, *args):
        for i in args:
            self.push(i)

    def __str__(self):
        if self.is_empty():
            return "[]"
        result = "["
        curr = self.head
        while curr != self.tail:
            result += f"{curr.data}, "
            curr = curr.next
        result += f"{self.tail.data}]"
        return result

    def reverse(self):
        if self.is_empty() or self.length == 1:
            return
        prev, curr = None, self.head
        while curr is not None:
            next_curr = curr.next
            curr.next = prev
            curr.prev = next_curr
            prev = curr
            curr = next_curr
        self.head, self.tail = self.tail, self.head
        return self.head, self.tail


class Solution:
    @staticmethod
    def reverse(dll: DoublyLinkedList, k: int = 0):
        if k == 1:
            return
        curr = temp = dll.head
        prev = None

        while curr is not None:
            # establish the part
            counter = 1
            length = 1
            while counter != k and temp.next is not None:
                temp = temp.next
                counter += 1
                length += 1
            next_curr = temp.next if temp.next is not None else None

            # disconnect the part from the rest of the DLL
            if temp is not None:
                temp.next = None

            # create a DLL out of the part
            sublist = DoublyLinkedList()
            sublist.head = curr
            sublist.tail = temp
            sublist.length = length

            # reverse the sublist part
            _head, _tail = sublist.reverse()

            if _tail == dll.head:
                dll.head = _head

            if _head == dll.tail:
                dll.tail = _tail

            # reconnect to the rest of DLL
            if prev is not None:
                prev.next = _head
                _head.prev = prev
            sublist.tail.next = next_curr
            if next_curr is not None:
                next_curr.prev = sublist.tail

            prev = _tail
            curr = temp = next_curr


def test(k, *args):
    dll = DoublyLinkedList()
    dll.build(*args)
    print(dll)
    Solution.reverse(dll, k)
    print(dll)


test(2, 2, 1, 4, 3, 6, 5)
test(4, 1, 2, 3, 4, 5, 6)
test(0, 1, 2, 3)
test(3, 1, 2, 3, 4, 5, 6, 7, 8)
test(1, 1, 2, 3, 4, 5)
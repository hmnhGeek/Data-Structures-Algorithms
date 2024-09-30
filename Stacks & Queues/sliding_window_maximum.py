class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = self.tail = None
        self.length = 0

    def is_empty(self):
        return self.length == 0

    def get_front(self):
        if self.is_empty():
            return
        return self.head.data

    def get_back(self):
        if self.is_empty():
            return
        return self.tail.data

    def push_front(self, x):
        node = Node(x)
        if self.is_empty():
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.length += 1

    def pop_front(self):
        if self.is_empty():
            return
        item = self.head.data
        node = self.head
        self.head = self.head.next
        if self.head is not None:
            self.head.prev = None
        del node
        self.length -= 1
        return item

    def push_back(self, x):
        node = Node(x)
        if self.is_empty():
            self.head = self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.length += 1

    def pop_back(self):
        if self.is_empty():
            return
        item = self.tail.data
        node = self.tail
        self.tail = self.tail.prev
        if self.tail is not None:
            self.tail.next = None
        del node
        self.length -= 1
        return item

    def show(self):
        curr = self.head
        while curr is not None:
            print(curr.data, end=" ")
            curr = curr.next
        print()


def get_sliding_window_maximum(arr, k):
    n = len(arr)
    doubly_linked_list = DoublyLinkedList()
    result = DoublyLinkedList()
    for i in range(n):
        if not doubly_linked_list.is_empty() and doubly_linked_list.get_front() == i - k:
            doubly_linked_list.pop_front()
        while not doubly_linked_list.is_empty() and arr[doubly_linked_list.get_back()] <= arr[i]:
            doubly_linked_list.pop_back()
        doubly_linked_list.push_back(i)
        if i >= k - 1:
            result.push_back(arr[doubly_linked_list.get_front()])
    return result


result1 = get_sliding_window_maximum([1, 3, -1, -3, 5, 3, 6, 7], 3)
result1.show()
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = self.next = None


class Deque:
    def __init__(self):
        self.head = self.tail = None
        self.length = 0

    def is_empty(self):
        return self.length == 0

    def push_back(self, x):
        node = Node(x)
        if self.is_empty():
            self.head = self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.length += 1

    def push_front(self, x):
        node = Node(x)
        if self.is_empty():
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.length += 1

    def front(self):
        if self.is_empty():
            return
        return self.head.data

    def back(self):
        if self.is_empty():
            return
        return self.tail.data

    def pop_back(self):
        if self.is_empty():
            return
        item = self.tail.data
        self.tail = self.tail.prev
        self.length -= 1
        return item

    def pop_front(self):
        if self.is_empty():
            return
        item = self.head.data
        self.head = self.head.next
        self.length -= 1
        return item


class Solution:
    @staticmethod
    def get_sliding_window_maximum(arr, k):
        deque = Deque()
        i, n = 0, len(arr)
        result = []
        for i in range(n):
            while not deque.is_empty() and deque.front() <= i - k:
                deque.pop_front()
            while not deque.is_empty() and arr[i] > arr[deque.back()]:
                deque.pop_back()
            deque.push_back(i)
            if i >= k - 1:
                result.append(arr[deque.front()])
        return result


print(Solution.get_sliding_window_maximum([1, 2, 3, 1, 4, 5, 2, 3, 6], 3))
print(Solution.get_sliding_window_maximum([5, 1, 3, 4, 2, 6], 1))
print(Solution.get_sliding_window_maximum([1, 3, 2, 1, 7, 3], 3))
print(Solution.get_sliding_window_maximum([1, 3, -1, -3, 5, 3, 6, 7], 3))

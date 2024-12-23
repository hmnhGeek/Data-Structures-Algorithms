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

    def pop_back(self):
        if self.is_empty():
            return
        node = self.tail
        self.tail = self.tail.prev
        if self.tail is not None:
            self.tail.next = None
        del node
        self.length -= 1

    def pop_front(self):
        if self.is_empty():
            return
        node = self.head
        self.head = self.head.next
        if self.head is not None:
            self.head.prev = None
        del node
        self.length -= 1

    def front(self):
        if self.is_empty():
            return -1e6
        return self.head.data

    def back(self):
        if self.is_empty():
            return 1e6
        return self.tail.data


class Solution:
    @staticmethod
    def sliding_window_maximum(arr, k):
        dq = Deque()
        dq.push_back(arr[0])
        n = len(arr)
        result = []
        for i in range(1, k):
            while not dq.is_empty() and dq.back() < arr[i]:
                dq.pop_back()
            dq.push_back(arr[i])
        result.append(dq.front())
        for i in range(k, n):
            if arr[i - k] == dq.front():
                dq.pop_front()
            while not dq.is_empty() and dq.back() < arr[i]:
                dq.pop_back()
            dq.push_back(arr[i])
            result.append(dq.front())
        return result


print(Solution.sliding_window_maximum([1, 2, 3, 1, 4, 5], 3))
print(Solution.sliding_window_maximum([8, 5, 10, 7, 9, 4, 15, 12, 90, 13], 4))
print(Solution.sliding_window_maximum([20, 10, 30], 1))
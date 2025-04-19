class Node:
    def __init__(self, data):
        self.data = data
        self.prev = self.next = None


class Deque:
    def __init__(self):
        self.head = self.tail = None
        self.length = 0

    def push(self, x):
        node = Node(x)
        if self.length == 0:
            self.head = self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.length += 1

    def pop_front(self):
        if self.length == 0:
            return
        item = self.head.data
        node = self.head
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        del node
        self.length -= 1
        return item

    def pop_back(self):
        if self.length == 0:
            return
        item = self.tail.data
        node = self.tail
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        del node
        self.length -= 1
        return item

    def front(self):
        if self.length == 0:
            return
        return self.head.data

    def back(self):
        if self.length == 0:
            return
        return self.tail.data


class SlidingWindowUtils:
    @staticmethod
    def get_max(arr, k):
        if k <= 0:
            return
        n = len(arr)
        deque = Deque()
        result = []
        for i in range(k):
            elem = arr[i]
            while deque.length != 0 and deque.back() < elem:
                deque.pop_back()
            deque.push(elem)
        result.append(deque.front())
        for i in range(k, n):
            if arr[i - k] == deque.front():
                deque.pop_front()
            elem = arr[i]
            while deque.length != 0 and deque.back() < elem:
                deque.pop_back()
            deque.push(elem)
            result.append(deque.front())
        return result


print(SlidingWindowUtils.get_max([1, 3, -1, -3, 5, 3, 2, 1, 6], 3))
print(SlidingWindowUtils.get_max([2, 5, -1, 7, -3, -1, -2], 4))
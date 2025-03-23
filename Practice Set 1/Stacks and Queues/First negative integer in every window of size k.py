class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


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
            self.tail = node
        self.length += 1

    def pop_front(self):
        if self.is_empty():
            return
        item = self.head.data
        node = self.head
        self.head = self.head.next
        del node
        self.length -= 1
        return item

    def front(self):
        if self.is_empty():
            return 0
        return self.head.data


class Solution:
    @staticmethod
    def first_negative(arr, k):
        if k <= 0 or k > len(arr):
            return -1
        dq = Deque()
        i = j = 0
        result = []
        while j - i + 1 != k + 1:
            if arr[j] < 0:
                dq.push_back(arr[j])
            j += 1
        result.append(dq.front())
        j -= 1
        n = len(arr)
        while 1:
            if arr[i] < 0:
                dq.pop_front()
            i += 1
            j += 1
            if j >= n:
                return result
            if arr[j] < 0:
                dq.push_back(arr[j])
            result.append(dq.front())


print(Solution.first_negative([-8, 2, 3, -6, 10], 2))
print(Solution.first_negative([12, -1, -7, 8, -15, 30, 16, 28], 3))
print(Solution.first_negative([4, 0, 3, -12, 1], 3))
print(Solution.first_negative([45, 12, -6], 1))
print(Solution.first_negative([4, -7, 4, 6, 7, -11, 2, 4], 2))
print(Solution.first_negative([1, 2, 3], 10))

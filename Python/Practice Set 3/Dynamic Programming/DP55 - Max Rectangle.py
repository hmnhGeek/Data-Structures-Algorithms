class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
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
            node.next = self.head
            self.head = node
        self.length += 1

    def pop(self):
        if self.is_empty():
            return -1
        item = self.head.data
        node = self.head
        self.head = self.head.next
        del node
        self.length -= 1
        return item

    def top(self):
        if self.is_empty():
            return -1
        return self.head.data


class Solution:
    @staticmethod
    def _max_area_in_histogram(histogram):
        stack = Stack()
        n = len(histogram)
        max_area = 0
        for i in range(n):
            while not stack.is_empty() and histogram[stack.top()] > histogram[i]:
                bar = histogram[stack.pop()]
                rb = i
                lb = stack.top()
                area = bar * (rb - lb - 1)
                max_area = max(max_area, area)
            stack.push(i)
        while not stack.is_empty():
            bar = histogram[stack.pop()]
            lb = stack.top()
            area = bar * (n - lb - 1)
            max_area = max(max_area, area)
        return max_area

    @staticmethod
    def max_area_in_mtx(mtx):
        n, m = len(mtx), len(mtx[0])
        prev_row = [0] * m
        max_area = 0
        for i in range(n):
            histogram = [mtx[i][j] + prev_row[j] if mtx[i][j] == 1 else 0 for j in range(m)]
            area = Solution._max_area_in_histogram(histogram)
            max_area = max(max_area, area)
            prev_row = histogram
        return max_area


print("Testing max area in a matrix")
print(
    Solution.max_area_in_mtx(
        [
            [0, 1, 1, 0],
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 0, 0]
        ]
    )
)

print(
    Solution.max_area_in_mtx(
        [
            [0, 1, 1],
            [1, 1, 1],
            [0, 1, 1]
        ]
    )
)

print(
    Solution.max_area_in_mtx(
        [
            [1, 0, 1, 0, 0],
            [1, 0, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 0, 0, 1, 0]
        ]
    )
)
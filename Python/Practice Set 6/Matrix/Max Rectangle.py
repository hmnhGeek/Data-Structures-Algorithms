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
            return
        item = self.head.data
        self.head = self.head.next
        self.length -= 1
        return item

    def top(self):
        if self.is_empty():
            return
        return self.head.data


class Utility:
    @staticmethod
    def get_max_area_in_histogram(histogram):
        """
            Time complexity is O(n) and space complexity is O(n)
        """
        stack = Stack()
        max_area = 0
        for i in range(len(histogram)):
            while not stack.is_empty() and histogram[stack.top()] > histogram[i]:
                bar = histogram[stack.pop()]
                rb = i
                lb = stack.top() if not stack.is_empty() else -1
                area = bar * (rb - lb - 1)
                max_area = max(max_area, area)
            stack.push(i)
        while not stack.is_empty():
            bar = histogram[stack.pop()]
            rb = len(histogram)
            lb = stack.top() if not stack.is_empty() else -1
            area = bar * (rb - lb - 1)
            max_area = max(max_area, area)
        return max_area


class Solution:
    @staticmethod
    def max_rectangle(mtx):
        n, m = len(mtx), len(mtx[0])
        prev = [0] * m
        max_area = 0
        for i in range(n):
            histogram = Solution._get_histogram(mtx[i], prev, m)
            area = Utility.get_max_area_in_histogram(histogram)
            max_area = max(max_area, area)
            prev = [j for j in histogram]
        return max_area

    @staticmethod
    def _get_histogram(row, prev, m):
        histogram = []
        for i in range(m):
            if row[i] != 0:
                histogram.append(row[i] + prev[i])
            else:
                histogram.append(0)
        return histogram


print("Utility Check")
print(Utility.get_max_area_in_histogram([60, 20, 50, 40, 10, 50, 60]))
print(Utility.get_max_area_in_histogram([3, 5, 1, 7, 5, 9]))
print()

print("Solution")
print(
    Solution.max_rectangle(
        [
            [0, 1, 1, 0],
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 0, 0]
        ]
    )
)

print(
    Solution.max_rectangle(
        [[0, 1, 1],
         [1, 1, 1],
         [0, 1, 1]]
    )
)

print(
    Solution.max_rectangle(
        [
            [1, 0, 1, 0, 0],
            [1, 0, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 0, 0, 1, 0]
        ]
    )
)

print(
    Solution.max_rectangle(
        [
            [0]
        ]
    )
)

print(
    Solution.max_rectangle(
        [
            [1]
        ]
    )
)

print(
    Solution.max_rectangle(
        [
            [1, 0, 1, 1],
            [1, 0, 1, 1],
            [0, 1, 0, 1],
            [1, 1, 1, 1],
            [0, 0, 0, 1]
        ]
    )
)

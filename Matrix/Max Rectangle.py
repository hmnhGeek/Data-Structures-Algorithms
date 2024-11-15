class StackNode:
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
        node = StackNode(x)
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
        node = self.head
        self.head = self.head.next
        del node
        self.length -= 1
        return item

    def top(self):
        if self.is_empty():
            return -1
        return self.head.data


class MaxAreaCalculator:
    @staticmethod
    def find_max_area_in_histogram(histogram):
        stack = Stack()
        n = len(histogram)
        max_area = 0
        for i in range(n):
            while not stack.is_empty() and histogram[stack.top()] > histogram[i]:
                bar = stack.pop()
                right_boundary = i
                left_boundary = stack.top()
                area = (right_boundary - left_boundary - 1) * histogram[bar]
                max_area = max(max_area, area)
            stack.push(i)

        while not stack.is_empty():
            bar = stack.pop()
            right_boundary = n
            left_boundary = stack.top()
            area = (right_boundary - left_boundary - 1) * histogram[bar]
            max_area = max(max_area, area)

        return max_area


# Using the utility method to find max area in histogram.
print(MaxAreaCalculator.find_max_area_in_histogram([3, 5, 1, 7, 5, 9]))
print(MaxAreaCalculator.find_max_area_in_histogram([60, 20, 50, 40, 10, 50, 60]))
print(MaxAreaCalculator.find_max_area_in_histogram([2, 1, 5, 6, 2, 3]))
print(MaxAreaCalculator.find_max_area_in_histogram([2, 4]))

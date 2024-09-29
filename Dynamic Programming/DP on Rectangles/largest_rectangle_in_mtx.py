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

    def top(self):
        if self.is_empty():
            return - 1
        return self.head.data

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
        node = self.head
        self.head = self.head.next
        del node
        self.length -= 1
        return item


def get_largest_area(histogram):
    stack = Stack()
    max_area = 0
    n = len(histogram)
    for i in range(len(histogram)):
        while stack.top() != -1 and histogram[i] < histogram[stack.top()]:
            bar = stack.pop()
            area = histogram[bar] * ((i - 1) - (stack.top() + 1) + 1)
            max_area = max(max_area, area)
        else:
            stack.push(i)

    while not stack.is_empty():
        bar = stack.pop()
        area = histogram[bar] * ((n - 1) - (stack.top() + 1) + 1)
        max_area = max(max_area, area)

    return max_area


print(get_largest_area([3, 1, 5, 6, 2, 3]))
print(get_largest_area([2, 1, 5, 6, 2, 3]))
print(get_largest_area([2, 4]))
print(get_largest_area([60, 20, 50, 40, 10, 50, 60]))
print(get_largest_area([3, 5, 1, 7, 5, 9]))

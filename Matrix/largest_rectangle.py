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
            return -1
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


class Utility:
    def __init__(self):
        pass

    @staticmethod
    def get_largest_area_rectangle_in_histogram(histogram):
        # define a stack class, and store the maximum area as 0.
        stack = Stack()
        max_area = 0
        n = len(histogram)

        # loop on each bar in O(n) time
        for i in range(n):
            # while the stack is not empty and the top element on the stack >= current element
            while not stack.is_empty() and histogram[stack.top()] >= histogram[i]:
                # if ith element is smaller than top element, then ith bar can act as a right boundary
                # of the top element. The next top element on the stack can act as the left boundary
                # of the popped element because on the stack we are storing elements in a linearly
                # increasing fashion.
                bar = stack.pop()

                # calculate the area and update the max_area value.
                area = histogram[bar] * ((i - 1) - (stack.top() + 1) + 1)
                max_area = max(max_area, area)
            else:
                # otherwise, if the stack is empty or the top element is less than current element, push
                # the ith index on to the stack.
                stack.push(i)

        # while there are some elements left in the stack
        while not stack.is_empty():
            # for each popped bar, last index will act as the right boundary
            bar = stack.pop()
            area = histogram[bar] * ((n - 1) - (stack.top() + 1) + 1)
            max_area = max(max_area, area)

        # return the max area
        return max_area


print(Utility.get_largest_area_rectangle_in_histogram([60, 20, 50, 40, 10, 50, 60]))
print(Utility.get_largest_area_rectangle_in_histogram([3, 5, 1, 7, 5, 9]))
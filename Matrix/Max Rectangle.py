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
        """
            Overall time complexity is O(n) and space complexity is O(n).
        """

        # create a stack to solve this problem.
        stack = Stack()
        n = len(histogram)
        max_area = 0

        # iterate on all the indices of the array.
        for i in range(n):
            # if the stack is not empty and the top element is greater than the current element, i.e, by
            # inserting the current element on the stack, we break the linearly increasing order of stack
            # elements...
            while not stack.is_empty() and histogram[stack.top()] > histogram[i]:
                # pop the element from the stack... this will be the current bar to focus on.
                bar = stack.pop()

                # it's right and left boundaries shall be calculated.
                right_boundary = i
                left_boundary = stack.top()

                # find the area of the max rectangle that can form around this bar.
                area = (right_boundary - left_boundary - 1) * histogram[bar]

                # update the global max area.
                max_area = max(max_area, area)

            # finally, push the current element to the stack.
            stack.push(i)

        # at last, the stack will contain a subset of indices in linearly increasing order.
        while not stack.is_empty():
            # start popping each bar with right boundary as `n` and do similar computations as above and update
            # the max area globally.
            bar = stack.pop()
            right_boundary = n
            left_boundary = stack.top()
            area = (right_boundary - left_boundary - 1) * histogram[bar]
            max_area = max(max_area, area)

        # return the max area that was obtained.
        return max_area


print("Using the utility method to find max area in histogram.")
print(MaxAreaCalculator.find_max_area_in_histogram([3, 5, 1, 7, 5, 9]))
print(MaxAreaCalculator.find_max_area_in_histogram([60, 20, 50, 40, 10, 50, 60]))
print(MaxAreaCalculator.find_max_area_in_histogram([2, 1, 5, 6, 2, 3]))
print(MaxAreaCalculator.find_max_area_in_histogram([2, 4]))
print()



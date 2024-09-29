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
    """
        Overall time complexity is O(n) and space complexity is O(n).
    """

    # initialize and empty stack to hold data in a linearly increasing fashion.
    stack = Stack()
    max_area = 0
    n = len(histogram)

    # loop on the bars of the histogram
    for i in range(len(histogram)):
        # while the stack is not empty and the current (ith) bar is less than the top of the stack, then it means
        # that this ith bar can act as the right boundary of the top element of the stack. Also, the element just
        # prior to the top element on the stack can act as the left boundary of the top element.
        # Hence, we can calculate the area of the rectangle with top element as the height and width equal to
        # ((i - 1) - (top + 1) + 1).
        while not stack.is_empty() and histogram[i] < histogram[stack.top()]:
            # pop the top element so that the next top element act as the left boundary.
            bar = stack.pop()
            area = histogram[bar] * ((i - 1) - (stack.top() + 1) + 1)
            # then update the max area.
            max_area = max(max_area, area)
        else:
            # however, if the stack is empty or the ith bar >= top element, simply push the ith bar on to the stack.
            stack.push(i)

    # at the end, till the stack is not empty, we are sure that every top element on the stack will have a right
    # boundary as `n - 1` and the left boundary will be `top + 1`.
    while not stack.is_empty():
        bar = stack.pop()
        area = histogram[bar] * ((n - 1) - (stack.top() + 1) + 1)
        # update the max area accordingly.
        max_area = max(max_area, area)

    # finally return the max_area.
    return max_area


print(get_largest_area([3, 1, 5, 6, 2, 3]))
print(get_largest_area([2, 1, 5, 6, 2, 3]))
print(get_largest_area([2, 4]))
print(get_largest_area([60, 20, 50, 40, 10, 50, 60]))
print(get_largest_area([3, 5, 1, 7, 5, 9]))


def get_histogram(prior, current):
    for i in range(len(current)):
        prior[i] = prior[i] + current[i] if current[i] != 0 else 0
    return prior


def max_area_in_matrix(mtx):
    max_area = 0
    n, m = len(mtx), len(mtx[0])
    prior_row = [0]*m
    for i in range(n):
        current_row = mtx[i]
        histogram = get_histogram(prior_row, current_row)
        max_area = max(max_area, get_largest_area(histogram))
        prior_row = histogram
    return max_area


print(
    max_area_in_matrix(
        [
            [0, 1, 1, 0],
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 0, 0]
        ]
    )
)

print(
    max_area_in_matrix(
        [
            [0, 1, 1],
            [1, 1, 1],
            [0, 1, 1]
        ]
    )
)
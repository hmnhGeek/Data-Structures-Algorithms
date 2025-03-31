# Problem link - https://www.geeksforgeeks.org/maximum-size-rectangle-binary-sub-matrix-1s/
# Solution - https://www.youtube.com/watch?v=tOylVCugy9k&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=56


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
        node = self.head
        self.head = self.head.next
        del node
        self.length -= 1
        return item

    def top(self):
        if self.is_empty():
            return -1
        return self.head.data


class Histogram:
    @staticmethod
    def get_max_area(arr):
        """
            Time complexity is O(n) and space complexity is O(n) for the stack.
        """

        # create required variables.
        stack = Stack()
        n = len(arr)
        max_area = 0

        # loop in the array
        for i in range(n):
            # while the stack has some elements and top element is greater than ith element, we must pop, because we
            # want to maintain linearly increasing order in the stack.
            while not stack.is_empty() and arr[stack.top()] > arr[i]:
                # for the top element, ith bar will be the right boundary.
                right = i
                # get the bar, which is the top element on the stack.
                bar = arr[stack.pop()]
                # element just before the top (new top now), will be the left boundary of the bar.
                left = stack.top()
                # get the area formed by this bar and update max area.
                area = bar * (right - left - 1)
                max_area = max(max_area, area)
            # finally, once there is no greater element on top of the stack, push `i`.
            stack.push(i)

        # once the iteration is over, stack will contain all those elements whose right boundary is `n`.
        while not stack.is_empty():
            right = n
            bar = arr[stack.pop()]
            left = stack.top()
            area = bar * (right - left - 1)
            max_area = max(max_area, area)

        # return the max area.
        return max_area


print("Testing the histogram class")
print(Histogram.get_max_area([3, 1, 5, 6, 2, 3]))
print(Histogram.get_max_area([2, 1, 5, 6, 2, 3]))
print(Histogram.get_max_area([2, 4]))
print(Histogram.get_max_area([60, 20, 50, 40, 10, 50, 60]))
print(Histogram.get_max_area([3, 5, 1, 7, 5, 9]))
print()


class Solution:
    @staticmethod
    def max_area_in_mtx(mtx):
        """
            Time complexity is O(nm) and space complexity is O(m).
        """

        n, m = len(mtx), len(mtx[0])
        # create a previous row. It will take O(m) extra space.
        prev_row = [0]*m
        max_area = 0
        for i in range(n):
            # create a histogram with another O(m) space and update the max area.
            histogram = [prev_row[j] + mtx[i][j] if mtx[i][j] != 0 else 0 for j in range(m)]
            # get the max area in O(m) time and O(m) space.
            max_area = max(max_area, Histogram.get_max_area(histogram))
            # remember to update previous row.
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
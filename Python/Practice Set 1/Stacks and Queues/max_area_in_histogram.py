# Problem link - https://www.geeksforgeeks.org/problems/maximum-rectangular-area-in-a-histogram-1587115620/1


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
            return
        return self.head.data


class Solution:
    @staticmethod
    def get_max_area(arr):
        """
            Time complexity is O(n) and space complexity is O(n).
        """

        # define a stack and global max area variable
        stack = Stack()
        max_area = 0
        n = len(arr)

        # loop on all the bars
        for i in range(n):
            # we will try to maintain a linearly increasing order in the stack and if the new element being inserted is
            # smaller than the top, then this order is distorted.
            while not stack.is_empty() and arr[i] < arr[stack.top()]:
                # this means `i` is the right boundary of the top and its left boundary is just below it.
                right = i
                bar = arr[stack.pop()]
                left = stack.top() if not stack.is_empty() else -1
                # get the area and update max area.
                area = bar * (right - left - 1)
                max_area = max(area, max_area)
            stack.push(i)

        # now, unless the stack is not empty, continuously get the max area with right boundary as n for the leftovers.
        while not stack.is_empty():
            right = n
            bar = arr[stack.pop()]
            left = stack.top() if not stack.is_empty() else -1
            area = bar * (right - left - 1)
            max_area = max(area, max_area)
        # return the max area.
        return max_area


print(Solution.get_max_area([60, 20, 50, 40, 10, 50, 60]))
print(Solution.get_max_area([7, 2, 8, 9, 1, 3, 6, 5]))
print(Solution.get_max_area([3]))
print(Solution.get_max_area([2,1,5,6,2,3]))
print(Solution.get_max_area([2,4]))
print(Solution.get_max_area([1, 0, 1, 2, 2, 2, 2, 1, 0, 2]))
print(Solution.get_max_area([1, 2, 1, 0, 1, 1, 0, 0, 2, 2]))
print(Solution.get_max_area([8, 6, 3, 5, 0, 0, 4, 10, 2, 5]))
print(Solution.get_max_area([6, 1, 8, 10, 5, 7, 0, 4, 5, 8]))

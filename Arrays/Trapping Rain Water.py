# Problem link - https://www.geeksforgeeks.org/problems/trapping-rain-water-1587115621/1


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

    def clear(self):
        self.head = self.tail = None
        self.length = 0


class Solution:
    @staticmethod
    def _get_left_bounds(arr, stack: Stack):
        """
            Time complexity is O(n) and space complexity is O(n) but not because of stack because the stack
            will always hold just one element.
        """

        # initialize left boundary
        lb = [0] * len(arr)

        # loop in the array
        for i in range(len(arr)):
            # while the stack is not empty and top element < current element, pop from the stack continuously.
            while not stack.is_empty() and stack.top() < arr[i]:
                stack.pop()

            # assign the left bound as the top of the stack (which denotes the maximum value at left side of `i`).
            bound = 0 if stack.top() is None else stack.top()
            lb[i] = bound

            # if stack is empty, add the current bar as this would be the maximum on left now.
            if stack.is_empty():
                stack.push(arr[i])
        return lb

    @staticmethod
    def _get_right_bounds(arr, stack: Stack):
        """
            Same as left bound method but just from right side.
        """

        rb = [0] * len(arr)
        for i in range(-1, -len(arr) - 1, -1):
            while not stack.is_empty() and stack.top() < arr[i]:
                stack.pop()
            bound = 0 if stack.top() is None else stack.top()
            rb[i] = bound
            if stack.is_empty():
                stack.push(arr[i])
        return rb

    @staticmethod
    def trap_rainwater(arr):
        """
            Overall time complexity is O(n) and space complexity is O(n).
        """

        # create a stack to find left and right boundaries
        stack = Stack()

        # get the left bound in O(n) time and O(n) space.
        lb = Solution._get_left_bounds(arr, stack)
        # clear the stack in O(1) time.
        stack.clear()

        # get the right boundaries in O(n) time and space.
        rb = Solution._get_right_bounds(arr, stack)
        stack.clear()

        # now loop on the array
        n = len(arr)
        water_collected = 0
        for i in range(n):
            # if both bounds are present
            if lb[i] != 0 and rb[i] != 0:
                # collect the water
                water_collected += (min(lb[i], rb[i]) - arr[i])

        # return the collected water
        return water_collected


print("Better Solution")
print(Solution.trap_rainwater([3, 0, 1, 0, 4, 0, 2]))
print(Solution.trap_rainwater([3, 0, 2, 0, 4]))
print(Solution.trap_rainwater([1, 2, 3, 4]))
print(Solution.trap_rainwater([2, 1, 5, 3, 1, 0, 4]))
print(Solution.trap_rainwater([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
print(Solution.trap_rainwater([4, 2, 0, 3, 2, 5]))
print()


class OptimalSolution:
    @staticmethod
    def trap_rainwater(arr):
        """
            Time complexity is O(n) and space complexity is O(1).
        """

        n = len(arr)
        left_max, right_max, left, right, total_water = 0, 0, 0, n - 1, 0
        while left < right:
            # if left building <= right building
            if arr[left] <= arr[right]:
                # and there is boundary on the left
                if left_max > arr[left]:
                    # collect water from left bound
                    total_water += (left_max - arr[left])
                else:
                    left_max = arr[left]
                left += 1
            else:
                # if right building > left building
                if right_max > arr[right]:
                    # collect water from right bound
                    total_water += (right_max - arr[right])
                else:
                    right_max = arr[right]
                right -= 1
        return total_water


print("Optimal Solution")
print(OptimalSolution.trap_rainwater([3, 0, 1, 0, 4, 0, 2]))
print(OptimalSolution.trap_rainwater([3, 0, 2, 0, 4]))
print(OptimalSolution.trap_rainwater([1, 2, 3, 4]))
print(OptimalSolution.trap_rainwater([2, 1, 5, 3, 1, 0, 4]))
print(OptimalSolution.trap_rainwater([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
print(OptimalSolution.trap_rainwater([4, 2, 0, 3, 2, 5]))

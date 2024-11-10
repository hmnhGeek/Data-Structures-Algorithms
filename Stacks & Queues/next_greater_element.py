# Problem link - https://www.geeksforgeeks.org/problems/next-larger-element-1587115620/1


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

    def get_top(self):
        if self.is_empty():
            return
        return self.head.data


class Solution:
    @staticmethod
    def get_next_greater_elements(arr):
        """
            Time complexity is O(n) and space complexity is O(n).
        """

        # create required variables
        stack = Stack()
        n = len(arr)
        result = [None] * n

        # loop from the right side of the array.
        for i in range(-1, -n - 1, -1):
            # if the stack is empty, there is nothing greater on the right side.
            if stack.get_top() is None:
                result[i] = -1
                # push the element on the stack and continue.
                stack.push(arr[i])
                continue

            # if the stack is not empty and top element is <= current element, continuously pop...
            while not stack.is_empty() and stack.get_top() <= arr[i]:
                stack.pop()

            # if the stack got empty, there is nothing greater on the right.
            if stack.is_empty():
                result[i] = -1

            # or if the top is greater than current
            elif stack.get_top() > arr[i]:
                # assign top element of stack as right greater.
                result[i] = stack.get_top()

            # push the current element on the stack.
            stack.push(arr[i])

        # return the result
        return result


print(Solution.get_next_greater_elements([1, 3, 2, 4]))
print(Solution.get_next_greater_elements([6, 8, 0, 1, 3]))
print(Solution.get_next_greater_elements([10, 20, 30, 50]))
print(Solution.get_next_greater_elements([50, 40, 30, 10]))
print(Solution.get_next_greater_elements([4, 5, 2, 25]))
print(Solution.get_next_greater_elements([13, 7, 6, 12]))

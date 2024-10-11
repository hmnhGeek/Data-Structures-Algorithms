# Problem link - https://www.geeksforgeeks.org/next-smaller-element/


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
            return
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


class Solution:
    @staticmethod
    def next_smaller(arr):
        """
            Time complexity is O(n) and space complexity is also O(n).
        """

        # create a blank stack
        stack = Stack()
        # also create a blank result array of same length
        result = [None for i in range(len(arr))]

        # traverse the array from reverse direction as we are trying to find next smaller which lie on the right
        # side; therefore, we must first generate information on the right side.
        for i in range(len(arr) - 1, -1, -1):
            # while the stack is not empty and the top element on the stack is greater than or equal to the current
            # element. In that case, continuously pop from the stack.
            while not stack.is_empty() and arr[stack.top()] >= arr[i]:
                stack.pop()

            # since while condition has failed, check if the stack is empty now.
            if stack.is_empty():
                # if the stack is empty, there is nothing on the right which is smaller than the current element and
                # therefore, assign -1 at the same index in result.
                result[i] = -1

            # other reason for while loop to stop could be that the stack is not empty but the top element is smaller
            # than the current element. In this case, simply assign the top element at result[i].
            elif arr[stack.top()] < arr[i]:
                result[i] = arr[stack.top()]

            # in any case, at last push the index `i` into the stack.
            stack.push(i)

        # finally, return the result containing next smaller elements.
        return result


print(Solution.next_smaller([4, 8, 5, 2, 25]))
print(Solution.next_smaller([13, 7, 6, 12]))
# Problem link - https://www.geeksforgeeks.org/sliding-window-maximum-maximum-of-all-subarrays-of-size-k/


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = self.next = None


class Deque:
    def __init__(self):
        self.head = self.tail = None
        self.length = 0

    def is_empty(self):
        return self.length == 0

    def push_back(self, x):
        node = Node(x)
        if self.is_empty():
            self.head = self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.length += 1

    def pop_back(self):
        if self.is_empty():
            return
        node = self.tail
        self.tail = self.tail.prev
        if self.tail is not None:
            self.tail.next = None
        del node
        self.length -= 1

    def pop_front(self):
        if self.is_empty():
            return
        node = self.head
        self.head = self.head.next
        if self.head is not None:
            self.head.prev = None
        del node
        self.length -= 1

    def front(self):
        if self.is_empty():
            return -1e6
        return self.head.data

    def back(self):
        if self.is_empty():
            return 1e6
        return self.tail.data


class Solution:
    @staticmethod
    def sliding_window_maximum(arr, k):
        """
            Overall time complexity is O(n) and space complexity is O(k).
        """

        # create a deque and push 0th element from the array into it in O(1) time.
        dq = Deque()
        dq.push_back(arr[0])

        # create useful variables.
        n = len(arr)
        result = []

        # loop for the first k elements.
        for i in range(1, k):
            # we want to keep elements in dq in linearly decreasing fashion. Therefore, pop from back until we get an
            # element which is greater than ith element, or the dq gets empty.
            while not dq.is_empty() and dq.back() < arr[i]:
                dq.pop_back()
            # if any of the above happens, push ith element into dq from back side.
            dq.push_back(arr[i])

        # since we have populated dq for the first window, get the max element for the first window from the front of
        # the dq.
        result.append(dq.front())

        # now loop for the remaining windows from kth index
        for i in range(k, n):
            # if the element that is about to get removed is the front element of dq, then this element is no longer
            # needed in the dq; pop it from the front.
            if arr[i - k] == dq.front():
                dq.pop_front()

            # we want to keep elements in dq in linearly decreasing fashion. Therefore, pop from back until we get an
            # element which is greater than ith element, or the dq gets empty.
            while not dq.is_empty() and dq.back() < arr[i]:
                dq.pop_back()

            # if any of the above happens, push ith element into dq from back side.
            dq.push_back(arr[i])

            # for the current k-length window, get the max element from the front of the dq.
            result.append(dq.front())

        # return the final result.
        return result


print(Solution.sliding_window_maximum([1, 2, 3, 1, 4, 5], 3))
print(Solution.sliding_window_maximum([8, 5, 10, 7, 9, 4, 15, 12, 90, 13], 4))
print(Solution.sliding_window_maximum([20, 10, 30], 1))
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = self.next = None


class Deque:
    def __init__(self):
        self.head = self.tail = None
        self.length = 0

    def push(self, x):
        node = Node(x)
        if self.length == 0:
            self.head = self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.length += 1

    def pop_front(self):
        if self.length == 0:
            return
        item = self.head.data
        node = self.head
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        del node
        self.length -= 1
        return item

    def pop_back(self):
        if self.length == 0:
            return
        item = self.tail.data
        node = self.tail
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        del node
        self.length -= 1
        return item

    def front(self):
        if self.length == 0:
            return
        return self.head.data

    def back(self):
        if self.length == 0:
            return
        return self.tail.data


class SlidingWindowUtils:
    @staticmethod
    def get_max(arr, k):
        """
            Time complexity is O(n) and space complexity is O(n).
        """

        # edge case
        if k <= 0:
            return
        n = len(arr)

        # create a blank deque
        deque = Deque()

        # create a result array.
        result = []

        # loop just on the first window.
        for i in range(k):
            elem = arr[i]

            # continuously pop back from the deque to maintain a linearly decreasing order.
            while deque.length != 0 and deque.back() < elem:
                deque.pop_back()

            # once the last element of deque is >= current element, push the current element.
            deque.push(elem)

        # append the max value of first window.
        result.append(deque.front())

        # now loop on the remaining indices...
        for i in range(k, n):
            # if the (i - k)th element of the array (which is being removed), is the maximum element, then pop from the
            # front of the deque.
            if arr[i - k] == deque.front():
                deque.pop_front()

            # do the same as we did for the first window.
            elem = arr[i]
            while deque.length != 0 and deque.back() < elem:
                deque.pop_back()
            deque.push(elem)
            result.append(deque.front())

        # return the final result.
        return result

    @staticmethod
    def get_min(arr, k):
        """
            Time complexity is O(n) and space complexity is O(n).
        """

        # edge case
        if k <= 0:
            return
        n = len(arr)

        # create a blank deque
        deque = Deque()

        # create a result array.
        result = []

        # loop just on the first window.
        for i in range(k):
            elem = arr[i]

            # continuously pop back from the deque to maintain a linearly ascending order.
            while deque.length != 0 and deque.back() > elem:
                deque.pop_back()

            # once the last element of deque is <= current element, push the current element.
            deque.push(elem)

        # append the max value of first window.
        result.append(deque.front())

        # now loop on the remaining indices...
        for i in range(k, n):
            # if the (i - k)th element of the array (which is being removed), is the maximum element, then pop from the
            # front of the deque.
            if arr[i - k] == deque.front():
                deque.pop_front()

            # do the same as we did for the first window.
            elem = arr[i]
            while deque.length != 0 and deque.back() > elem:
                deque.pop_back()
            deque.push(elem)
            result.append(deque.front())

        # return the final result.
        return result


class Solution:
    @staticmethod
    def solve(arr, k):
        maxi = SlidingWindowUtils.get_max(arr, k)
        mini = SlidingWindowUtils.get_min(arr, k)
        return sum(maxi) + sum(mini)


print(Solution.solve([2, 5, -1, 7, -3, -1, -2], 4))
print(Solution.solve([1, 2, 3, 4, 5], 3))
print(Solution.solve([2, 4, 7, 3, 8, 1], 4))

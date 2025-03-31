# Problem link - https://www.geeksforgeeks.org/problems/first-negative-integer-in-every-window-of-size-k3345/1
# Solution - https://www.youtube.com/watch?v=-uc7OCrjp8g


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


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
            self.tail = node
        self.length += 1

    def pop_front(self):
        if self.is_empty():
            return
        item = self.head.data
        node = self.head
        self.head = self.head.next
        del node
        self.length -= 1
        return item

    def front(self):
        if self.is_empty():
            return 0
        return self.head.data


class Solution:
    @staticmethod
    def first_negative(arr, k):
        """
            Time complexity is O(n) and space complexity is O(k).
        """

        # edge cases
        if k <= 0 or k > len(arr):
            return -1

        # create a deque
        dq = Deque()

        # define i and j pointing to the 0th index.
        i = j = 0

        # define a result variable.
        result = []

        # while we don't achieve the first window in O(k) time.
        while j - i + 1 != k + 1:
            # push negative numbers into the deque in O(1) time.
            if arr[j] < 0:
                dq.push_back(arr[j])
            j += 1

        # after the first window is achieved, push the front element from deque into the result variable.
        result.append(dq.front())

        # bring `j` back to 1 unit, because in previous loop we ran till `k + 1` size.
        j -= 1
        n = len(arr)

        # loop in the remaining windows in apx n iterations.
        while 1:
            # if the front element of the window is negative, pop front from deque in O(1) time.
            if arr[i] < 0:
                dq.pop_front()

            # increment to the next window.
            i += 1
            j += 1

            # if `j` is out of bounds, return the answer.
            if j >= n:
                return result

            # else, if j element is negative, push to deque.
            if arr[j] < 0:
                dq.push_back(arr[j])

            # and append the first negative from deque.
            result.append(dq.front())


print(Solution.first_negative([-8, 2, 3, -6, 10], 2))
print(Solution.first_negative([12, -1, -7, 8, -15, 30, 16, 28], 3))
print(Solution.first_negative([4, 0, 3, -12, 1], 3))
print(Solution.first_negative([45, 12, -6], 1))
print(Solution.first_negative([4, -7, 4, 6, 7, -11, 2, 4], 2))
print(Solution.first_negative([1, 2, 3], 10))

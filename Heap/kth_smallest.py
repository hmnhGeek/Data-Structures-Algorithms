# Problem link - https://www.geeksforgeeks.org/kth-smallest-largest-element-in-unsorted-array/


class MaxHeap:
    def __init__(self):
        self.heap = []

    def is_empty(self):
        return len(self.heap) == 0

    def get_lci(self, pi):
        lci = 2 * pi + 1
        return lci if lci in range(len(self.heap)) else None

    def get_rci(self, pi):
        rci = 2 * pi + 2
        return rci if rci in range(len(self.heap)) else None

    def get_pi(self, ci):
        if ci == 0:
            return
        pi = int((ci - 1) / 2)
        return pi if pi in range(len(self.heap)) else None

    def get_max_child_index(self, lci, rci):
        if lci is None and rci is None:
            return
        if lci is None:
            return rci
        if rci is None:
            return lci
        max_child_index = lci
        if self.heap[rci] > self.heap[max_child_index]:
            max_child_index = rci
        return max_child_index

    def max_heapify_up(self, start_index):
        if start_index == 0:
            return
        pi = self.get_pi(start_index)
        lci, rci = self.get_lci(pi), self.get_rci(pi)
        max_child_index = self.get_max_child_index(lci, rci)
        if max_child_index is not None:
            if self.heap[pi] < self.heap[max_child_index]:
                self.heap[pi], self.heap[max_child_index] = self.heap[max_child_index], self.heap[pi]
            self.max_heapify_up(pi)

    def max_heapify_down(self, pi):
        lci, rci = self.get_lci(pi), self.get_rci(pi)
        max_child_index = self.get_max_child_index(lci, rci)
        if max_child_index is not None:
            if self.heap[pi] < self.heap[max_child_index]:
                self.heap[pi], self.heap[max_child_index] = self.heap[max_child_index], self.heap[pi]
            self.max_heapify_down(max_child_index)

    def push(self, x):
        self.heap.append(x)
        self.max_heapify_up(len(self.heap) - 1)

    def pop(self):
        if self.is_empty():
            return
        item = self.heap[0]
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        del self.heap[-1]
        self.max_heapify_down(0)
        return item


class Solution:
    @staticmethod
    def get_kth_smallest(arr, k):
        """
            Overall time complexity is O((n - k)*log(k) + k*log(k)) = O(n*log(k))
            Overall space complexity is O(k) for the max heap.
        """

        # if k is out of bounds, return None.
        if k > len(arr) or k <= 0:
            return

        # initialize an empty max heap.
        max_heap = MaxHeap()

        # push first k elements from the array into the stack in O(k*log(k)) time.
        for i in range(k):
            max_heap.push(arr[i])

        # iterate from kth element till end of the array. This will take O((n - k)*log(k))
        for i in range(k, len(arr)):
            # if the ith element is smaller than the top of the max heap, it could be
            # a potential candidate for kth smallest. Pop the top of max heap and push
            # this element on the max heap. Both operations will take O(log(k)) time.
            if arr[i] < max_heap.heap[0]:
                max_heap.pop()
                max_heap.push(arr[i])

        # return the kth smallest in O(1) time from the top of the max heap.
        return max_heap.heap[0]


print(Solution.get_kth_smallest([7, 10, 4, 3, 20, 15], 3))
print(Solution.get_kth_smallest([7, 10, 4, 3, 20, 15], 4))
print(Solution.get_kth_smallest([10, 5, 4, 3, 48, 6, 2, 33, 53, 10], 4))
print(Solution.get_kth_smallest([1, 2, 6, 4, 5, 3], 3))
print(Solution.get_kth_smallest([1, 2, 6, 4, 5], 3))
print(Solution.get_kth_smallest([1, 5, 7, 6, 4, 3, 2], 3))
print(Solution.get_kth_smallest([1], 1))

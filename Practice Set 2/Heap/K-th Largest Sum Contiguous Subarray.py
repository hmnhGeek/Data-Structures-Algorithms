# Problem link - https://www.geeksforgeeks.org/k-th-largest-sum-contiguous-subarray/
# Solution - https://www.youtube.com/watch?v=Rb4jGawY0MA&t=367s


class MinHeap:
    def __init__(self):
        self.heap = []

    def is_empty(self):
        return len(self.heap) == 0

    def get_lci(self, pi):
        lci = 2*pi + 1
        return lci if lci in range(len(self.heap)) else None

    def get_rci(self, pi):
        rci = 2*pi + 2
        return rci if rci in range(len(self.heap)) else None

    def get_pi(self, ci):
        if ci == 0:
            return
        pi = int((ci - 1)/2)
        return pi if pi in range(len(self.heap)) else None

    def get_min_child_index(self, lci, rci):
        if lci is None and rci is None:
            return
        if lci is None:
            return rci
        if rci is None:
            return lci
        min_child_index = lci
        if self.heap[rci] < self.heap[min_child_index]:
            min_child_index = rci
        return min_child_index

    def min_heapify_up(self, start_index):
        if start_index == 0:
            return
        pi = self.get_pi(start_index)
        lci, rci = self.get_lci(pi), self.get_rci(pi)
        min_child_index = self.get_min_child_index(lci, rci)
        if min_child_index is not None:
            if self.heap[pi] > self.heap[min_child_index]:
                self.heap[pi], self.heap[min_child_index] = self.heap[min_child_index], self.heap[pi]
            self.min_heapify_up(pi)

    def min_heapify_down(self, pi):
        lci, rci = self.get_lci(pi), self.get_rci(pi)
        min_child_index = self.get_min_child_index(lci, rci)
        if min_child_index is not None:
            if self.heap[pi] > self.heap[min_child_index]:
                self.heap[pi], self.heap[min_child_index] = self.heap[min_child_index], self.heap[pi]
            self.min_heapify_down(min_child_index)

    def insert(self, x):
        self.heap.append(x)
        self.min_heapify_up(len(self.heap) - 1)

    def pop(self):
        if self.is_empty():
            return
        item = self.heap[0]
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        del self.heap[-1]
        self.min_heapify_down(0)
        return item


class Solution:
    @staticmethod
    def _get_subarray_sums(arr, subarray_sums):
        n = len(arr)
        for i in range(n):
            _sum = arr[i]
            subarray_sums.append(_sum)
            for j in range(i + 1, n):
                _sum += arr[j]
                subarray_sums.append(_sum)

    @staticmethod
    def kth_largest(arr, k):
        """
            Time complexity is O(n^2) and space complexity is O(n^2).
        """

        # in O(n^2) and O(n^2) space, get the subarray sum.
        subarray_sums = []
        Solution._get_subarray_sums(arr, subarray_sums)

        # push first `k` items in the min heap in O(k * log(k)) time and O(k) space.
        min_heap = MinHeap()
        for i in range(k):
            min_heap.insert(subarray_sums[i])

        # start from the kth index, in O(n * log(k))
        i = k
        while i < len(subarray_sums):
            # if the top < ith element, pop the top and push ith element in O(2 * log(k))
            top = min_heap.heap[0]
            if top < subarray_sums[i]:
                min_heap.pop()
                min_heap.insert(subarray_sums[i])
            i += 1
        return min_heap.heap[0]


print(Solution.kth_largest([20, -5, -1], 3))
print(Solution.kth_largest([10, -10, 20, -40], 6))
print(Solution.kth_largest([3, 2, 1], 2))
print(Solution.kth_largest([2, 6, 4, 1], 3))
print(Solution.kth_largest([1, -2, 3, -4, 5], 2))
print(Solution.kth_largest([3, -2, 5], 3))
print(Solution.kth_largest([4, 1], 2))
print(Solution.kth_largest([5, 4, -8, 6], 10))

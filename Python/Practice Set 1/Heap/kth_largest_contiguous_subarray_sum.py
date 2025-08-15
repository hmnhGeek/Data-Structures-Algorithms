# Problem link - https://www.geeksforgeeks.org/dsa/k-th-largest-sum-contiguous-subarray/
# Solution - https://www.youtube.com/watch?v=lTmaCCOlQ90
# Prefix sums - https://www.youtube.com/watch?v=PhgtNY_-CiY


class MinHeap:
    def __init__(self):
        self.heap = []

    def __len__(self):
        return len(self.heap)

    def is_empty(self):
        return self.__len__() == 0

    def get_lci(self, pi):
        lci = 2 * pi + 1
        return lci if lci in range(self.__len__()) else None

    def get_rci(self, pi):
        rci = 2 * pi + 2
        return rci if rci in range(self.__len__()) else None

    def get_pi(self, ci):
        if ci == 0:
            return None
        pi = int((ci - 1) / 2)
        return pi if pi in range(self.__len__()) else None

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

    def top(self):
        if self.is_empty():
            return
        return self.heap[0]


class Solution:
    @staticmethod
    def get_heap_top(pq: MinHeap):
        top = pq.top()
        return top if top else -1e6

    @staticmethod
    def find_kth_largest(arr, k):
        """
            Time complexity is O(n^2 * log(k)) and space complexity is O(n).
        """

        pq = MinHeap()

        # The prefix sums array occupies O(n) space only and its computation takes O(n^2) time.
        prefix_sums = Solution._get_prefix_sums(arr)

        # loop for n^2 times on prefix sums to generate all the subarray sums
        for i in range(len(prefix_sums) - 1):
            for j in range(i + 1, len(prefix_sums)):
                _sum = prefix_sums[j] - prefix_sums[i]

                # get the top of the heap in O(1) time.
                top = Solution.get_heap_top(pq)

                # if there is space in heap, simply insert the sum and move to next iteration.
                # This will take O(log(k)) time.
                if len(pq) < k:
                    pq.insert(_sum)
                    continue

                # now, only replace the top element with this one if top element is smaller than the current
                # sum. Again, this will take O(2 * log(k)) time.
                if _sum > top:
                    pq.pop()
                    pq.insert(_sum)

        # The kth largest will be on the top of the heap.
        return Solution.get_heap_top(pq)

    @staticmethod
    def _get_prefix_sums(arr):
        result = [0]
        for i in arr:
            result.append(result[-1] + i)
        return result


print(Solution.find_kth_largest([20, -5, -1], 3))
print(Solution.find_kth_largest([10, -10, 20, -40], 6))
print(Solution.find_kth_largest([3, 2, 1], 2))
print(Solution.find_kth_largest([2, 6, 4, 1], 3))

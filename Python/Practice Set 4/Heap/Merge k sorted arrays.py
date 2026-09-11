# Problem link - https://www.geeksforgeeks.org/problems/merge-k-sorted-arrays/1


class MinHeap:
    def __init__(self):
        self.heap = []

    def is_empty(self):
        return len(self.heap) == 0

    def get_lci(self, pi):
        ci = 2*pi + 1
        if 0 <= ci < len(self.heap):
            return ci
        return None

    def get_rci(self, pi):
        ci = 2*pi + 2
        if 0 <= ci < len(self.heap):
            return ci
        return None

    def get_pi(self, ci):
        pi = int((ci - 1)/2)
        if 0 <= pi < len(self.heap):
            return pi
        return None

    def get_min_child_index(self, lci, rci):
        if lci is None and rci is None:
            return
        if lci is None:
            return rci
        if rci is None:
            return lci
        mci = lci
        if self.heap[rci] < self.heap[mci]:
            mci = rci
        return mci

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
    def merge_k_sorted_lists(mtx):
        """
            Time complexity is O(n * log(k)) and space complexity is O(k).
        """
        n = len(mtx)
        if n == 0:
            return []
        pq = MinHeap()
        for i in range(n):
            if len(mtx[i]) != 0:
                pq.insert((mtx[i][0], i, 0))
        result = []
        while not pq.is_empty():
            elem, i, j = pq.pop()
            result.append(elem)
            if 0 <= j + 1 < len(mtx[i]):
                pq.insert((mtx[i][j + 1], i, j + 1))
        return result


print(
    Solution.merge_k_sorted_lists(
        [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
    )
)

print(
    Solution.merge_k_sorted_lists(
        [
            [1, 4, 5],
            [1, 3, 4],
            [2, 6]
        ]
    )
)

print(
    Solution.merge_k_sorted_lists([])
)

print(
    Solution.merge_k_sorted_lists([[]])
)

print(
    Solution.merge_k_sorted_lists(
        [
            [1],
            [2, 4],
            [3, 7, 9, 11],
            [13]
        ]
    )
)

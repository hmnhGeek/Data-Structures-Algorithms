class MinHeap:
    def __init__(self):
        self.heap = []

    def is_empty(self):
        return len(self.heap)

    def get_lci(self, pi):
        ci = 2*pi + 1
        return ci if 0 <= ci < len(self.heap) else None

    def get_rci(self, pi):
        ci = 2 * pi + 2
        return ci if 0 <= ci < len(self.heap) else None

    def get_pi(self, ci):
        pi = int((ci - 1)/2)
        return pi if 0 <= pi < len(self.heap) else None

    def get_min_child_index(self, lci, rci):
        if lci is None and rci is None:
            return None
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
        mci = self.get_min_child_index(lci, rci)
        if mci is not None:
            if self.heap[pi] > self.heap[mci]:
                self.heap[pi], self.heap[mci] = self.heap[mci], self.heap[pi]
            self.min_heapify_up(pi)

    def min_heapify_down(self, pi):
        lci, rci = self.get_lci(pi), self.get_rci(pi)
        mci = self.get_min_child_index(lci, rci)
        if mci is not None:
            if self.heap[pi] > self.heap[mci]:
                self.heap[pi], self.heap[mci] = self.heap[mci], self.heap[pi]
            self.min_heapify_up(mci)

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
    def get_kth_largest_sum(arr, k):
        if arr is None or len(arr) == 0:
            return
        if k is None or k <= 0:
            return
        sub_array_sums = Solution._get_sub_array_sums(arr)
        pq = MinHeap()
        for i in range(k):
            pq.insert(arr[i])
        i = k
        while i < len(arr):
            if arr[i] > pq.heap[0]:
                pq.pop()
                pq.insert(arr[i])
            i += 1
        return pq.pop()


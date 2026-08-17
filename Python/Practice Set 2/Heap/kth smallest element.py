# Problem link - https://www.geeksforgeeks.org/kth-smallest-largest-element-in-unsorted-array/


class MaxHeap:
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

    def get_max_child_index(self, lci, rci):
        if lci is None and rci is None:
            return
        if lci is None:
            return rci
        if rci is None:
            return lci
        mci = lci
        if self.heap[rci] > self.heap[mci]:
            mci = rci
        return mci

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
            self.max_heapify_up(pi)

    def insert(self, x):
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
            Time complexity is O(n * log(k)) and space complexity is O(k).
        """
        if k <= 0:
            return
        pq = MaxHeap()
        for i in range(k):
            pq.insert(arr[i])
        i = k
        while i < len(arr):
            if arr[i] < pq.heap[0]:
                pq.pop()
                pq.insert(arr[i])
            i += 1
        return pq.pop()


print(Solution.get_kth_smallest([7, 10, 4, 3, 20, 15], 3))
print(Solution.get_kth_smallest([7, 10, 4, 3, 20, 15], 4))
print(Solution.get_kth_smallest([1, 2, 6, 4, 5, 3], 3))
print(Solution.get_kth_smallest([1, 2, 6, 4, 5], 3))
print(Solution.get_kth_smallest([3, 2, 1, 5, 6, 4], 2))
print(Solution.get_kth_smallest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
print(Solution.get_kth_smallest([1, 23, 12, 9, 30, 2, 50], 3))
print(Solution.get_kth_smallest([11, 5, 12, 9, 44, 17, 2], 2))

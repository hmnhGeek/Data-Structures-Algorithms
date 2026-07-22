# Problem link - http://geeksforgeeks.org/problems/median-in-a-row-wise-sorted-matrix1527/1


class MinHeap:
    def __init__(self):
        self.heap = []

    def is_empty(self):
        return len(self.heap) == 0

    def get_lci(self, pi):
        ci = 2*pi + 1
        return ci if ci in range(len(self.heap)) else None

    def get_rci(self, pi):
        ci = 2 * pi + 2
        return ci if ci in range(len(self.heap)) else None

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
    def get_median(mtx):
        """
            Time complexity is O(nm * log(n)) and space complexity is O(n).
        """
        pq = MinHeap()
        n, m = len(mtx), len(mtx[0])
        median_pt = ((n * m) // 2) + 1
        for i in range(n):
            pq.insert((mtx[i][0], i, 0))
        counter = 0
        while not pq.is_empty():
            elem, i, j = pq.pop()
            counter += 1
            if counter == median_pt:
                return elem
            if 0 <= j + 1 < m:
                pq.insert((mtx[i][j + 1], i, j + 1))
        return -1


print(Solution.get_median([[1, 3, 5], [2, 6, 9], [3, 6, 9]]))
print(Solution.get_median([[1], [2], [3]]))
print(Solution.get_median([[3], [5], [8]]))

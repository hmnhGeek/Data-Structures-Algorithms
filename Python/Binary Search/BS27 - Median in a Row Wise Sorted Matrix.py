# Problem link - https://www.naukri.com/code360/problems/median-of-a-row-wise-sorted-matrix_1115473
# Solution - https://www.youtube.com/watch?v=Q9wXgdxJq48&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=29


class MinHeap:
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

    def get_min_child_index(self, lci, rci):
        if lci is None and rci is None:
            return
        if lci is None:
            return rci
        if rci is None:
            return lci
        min_child_index = lci
        if self.heap[rci][0] < self.heap[min_child_index][0]:
            min_child_index = rci
        return min_child_index

    def min_heapify_up(self, start_index):
        if start_index == 0:
            return
        pi = self.get_pi(start_index)
        lci, rci = self.get_lci(pi), self.get_rci(pi)
        min_child_index = self.get_min_child_index(lci, rci)
        if min_child_index is not None:
            if self.heap[pi][0] > self.heap[min_child_index][0]:
                self.heap[pi], self.heap[min_child_index] = self.heap[min_child_index], self.heap[pi]
            self.min_heapify_up(pi)

    def min_heapify_down(self, pi):
        lci, rci = self.get_lci(pi), self.get_rci(pi)
        min_child_index = self.get_min_child_index(lci, rci)
        if min_child_index is not None:
            if self.heap[pi][0] > self.heap[min_child_index][0]:
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
            Time complexity is O(m*log(n)) and space complexity is O(n).
        """

        n, m = len(mtx), len(mtx[0])
        min_heap = MinHeap()
        # push first column in O(log(n)) time.
        for i in range(n):
            min_heap.insert((mtx[i][0], i, 0))
        counter = 0
        median_index = (n * m + 1) // 2

        # this will run for m time.
        while not min_heap.is_empty():
            # this will take O(log(n)) time.
            elem, x, y = min_heap.pop()
            counter += 1
            if counter == median_index:
                return elem
            # another O(log(n)) time.
            if 0 <= y + 1 < m:
                min_heap.insert((mtx[x][y + 1], x, y + 1))
        return -1


print(
    Solution.get_median(
        [
            [1, 3, 5],
            [2, 6, 9],
            [3, 6, 9]
        ]
    )
)

print(
    Solution.get_median(
        [
            [1, 3, 4],
            [2, 5, 6],
            [7, 8, 9]
        ]
    )
)

print(
    Solution.get_median(
        [[1, 5, 7, 9, 11],
         [2, 3, 4, 8, 9],
         [4, 11, 14, 19, 20],
         [6, 10, 22, 99, 100],
         [7, 15, 17, 24, 28]]
    )
)

print(
    Solution.get_median(
        [
            [1, 2, 3, 4, 5],
            [8, 9, 11, 12, 13],
            [21, 23, 25, 27, 29]
        ]
    )
)

print(Solution.get_median([[1], [2], [3]]))
print(Solution.get_median([[3], [5], [8]]))

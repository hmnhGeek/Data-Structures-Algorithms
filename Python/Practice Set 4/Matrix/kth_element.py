# Problem link - https://www.geeksforgeeks.org/problems/kth-element-in-matrix/1


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
    def get_kth_element(mtx, k):
        """
            Time complexity is O({n + k} * log(n)) time and O(n) space.
        """

        # get the dimensions of the matrix
        n, m = len(mtx), len(mtx[0])

        # edge case
        if k not in range(1, n * m + 1):
            return -1

        # initialize a priority queue
        pq = MinHeap()

        # push the first column into the matrix in O(n * log(n))
        for i in range(n):
            pq.insert((mtx[i][0], i, 0))

        # initialize a counter variable to track `k`.
        counter = 0

        # while the pq is not empty. This will run for k-iterations.
        while not pq.is_empty():
            # get the element from heap in O(log(n)) time.
            elem, x, y = pq.pop()
            counter += 1

            # if counter has become `k`, return the element.
            if counter == k:
                return elem

            # push the next element in O(log(n)) time.
            if 0 <= y + 1 < m:
                pq.insert((mtx[x][y + 1], x, y + 1))
        return -1


print(
    Solution.get_kth_element(
        [
            [16, 28, 60, 64],
            [22, 41, 63, 91],
            [27, 50, 87, 93],
            [36, 78, 87, 94]
        ],
        3
    )
)

print(
    Solution.get_kth_element(
        [
            [16, 28, 60, 64],
            [22, 41, 63, 91],
            [27, 50, 87, 93],
            [36, 78, 87, 94]
        ],
        100
    )
)

print(
    Solution.get_kth_element(
        [
            [16, 28, 60, 64],
            [22, 41, 63, 91],
            [27, 50, 87, 93],
            [36, 78, 87, 94]
        ],
        -10
    )
)

print(
    Solution.get_kth_element(
        [
            [10, 20, 30, 40],
            [15, 25, 35, 45],
            [24, 29, 37, 48],
            [32, 33, 39, 50]
        ],
        7
    )
)

print(
    Solution.get_kth_element(
        [
            [10, 20, 30, 40],
            [15, 25, 35, 45],
            [24, 29, 37, 48],
            [32, 33, 39, 50]
        ],
        15
    )
)

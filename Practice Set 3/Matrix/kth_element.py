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

        n = len(mtx)

        # edge case
        if k <= 0:
            return

        # create a min heap and push the first column elements into it in O(n * log(n)) time and O(n) space.
        min_heap = MinHeap()
        for i in range(n):
            min_heap.insert((mtx[i][0], i, 0))

        # create a counter variable to track `k` elements
        counter = 0
        element = -1

        # typical min heap condition. This will ideally run for k times.
        while not min_heap.is_empty():
            # pop the current element from the heap in O(log(n)) time.
            element, i, j = min_heap.pop()
            # increment the counter
            counter += 1

            # if counter matches k, return the current element.
            if counter == k:
                return element

            # else push the next cell from the popped element's row. This will take O(log(n)) time.
            if 0 <= j + 1 < n:
                min_heap.insert((mtx[i][j + 1], i, j + 1))

        # return the max element from the matrix in case k > n^2.
        return element


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
# Problem link - https://www.geeksforgeeks.org/problems/median-in-a-row-wise-sorted-matrix1527/1


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


class Matrix:
    @staticmethod
    def median_finder(mtx):
        """
            Time complexity is O(m*n*log(n)) and space complexity is O(n).
        """

        n, m = len(mtx), len(mtx[0])
        min_heap = MinHeap()
        counter = 0
        median_counter = (n*m)//2 + 1

        for i in range(n):
            min_heap.insert((mtx[i][0], i, 0))

        while not min_heap.is_empty():
            item, i, j = min_heap.pop()
            counter += 1
            if counter == median_counter:
                return item

            if 0 <= j + 1 < m:
                min_heap.insert((mtx[i][j + 1], i, j + 1))


print(
    Matrix.median_finder(
        [
            [1, 3, 5],
            [2, 6, 9],
            [3, 6, 9]
        ]
    )
)

print(
    Matrix.median_finder(
        [
            [1],
            [2],
            [3]
        ]
    )
)
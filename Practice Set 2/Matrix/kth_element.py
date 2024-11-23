from typing import List, Optional


class HeapElement:
    def __init__(self, data, x, y):
        self.__data = data
        self.__x = x
        self.__y = y

    def get_data(self):
        return self.__data

    def get_row_index(self):
        return self.__x

    def get_col_index(self):
        return self.__y


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
        if self.heap[rci].get_data() < self.heap[min_child_index].get_data():
            min_child_index = rci
        return min_child_index

    def min_heapify_up(self, start_index):
        if start_index == 0:
            return
        pi = self.get_pi(start_index)
        lci, rci = self.get_lci(pi), self.get_rci(pi)
        min_child_index = self.get_min_child_index(lci, rci)
        if min_child_index is not None:
            if self.heap[pi].get_data() > self.heap[min_child_index].get_data():
                self.heap[pi], self.heap[min_child_index] = self.heap[min_child_index], self.heap[pi]
            self.min_heapify_up(pi)

    def min_heapify_down(self, pi):
        lci, rci = self.get_lci(pi), self.get_rci(pi)
        min_child_index = self.get_min_child_index(lci, rci)
        if min_child_index is not None:
            if self.heap[pi].get_data() > self.heap[min_child_index].get_data():
                self.heap[pi], self.heap[min_child_index] = self.heap[min_child_index], self.heap[pi]
            self.min_heapify_down(min_child_index)

    def insert(self, x: HeapElement):
        self.heap.append(x)
        self.min_heapify_up(len(self.heap) - 1)

    def pop(self) -> Optional[HeapElement]:
        if self.is_empty():
            return
        item = self.heap[0]
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        del self.heap[-1]
        self.min_heapify_down(0)
        return item


class Solution:
    @staticmethod
    def get_kth_element(mtx: List[List[int]], k: int) -> Optional[int]:
        n = len(mtx)
        if k > n**2:
            return mtx[-1][-1]
        if k < 0:
            return
        min_heap = MinHeap()
        for i in range(n):
            min_heap.insert(HeapElement(mtx[i][0], i, 0))
        counter = 0
        while counter != k:
            heap_element = min_heap.pop()
            counter += 1
            if counter == k:
                return heap_element.get_data()
            i, j = heap_element.get_row_index(), heap_element.get_col_index()
            if 0 <= j + 1 < n:
                min_heap.insert(HeapElement(mtx[i][j + 1], i, j + 1))
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

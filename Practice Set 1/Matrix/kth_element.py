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
        if rci is None:
            return lci
        if lci is None:
            return rci
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

    def push(self, x):
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
    def get_kth(mtx, k):
        n, m = len(mtx), len(mtx[0])
        if k not in range(1, n * m + 1):
            return
        min_heap = MinHeap()
        for i in range(n):
            min_heap.push((mtx[i][0], i, 0))

        counter = 0
        while not min_heap.is_empty():
            elem, x, y = min_heap.pop()
            counter += 1
            if counter == k:
                return elem
            if 0 <= y + 1 < m:
                min_heap.push((mtx[x][y + 1], x, y + 1))


print(
    Matrix.get_kth(
        [[16, 28, 60, 64],
         [22, 41, 63, 91],
         [27, 50, 87, 93],
         [36, 78, 87, 94]],
        3
    )
)

print(
    Matrix.get_kth(
        [[10, 20, 30, 40],
         [15, 25, 35, 45],
         [24, 29, 37, 48],
         [32, 33, 39, 50]],
        7
    )
)

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
        if self.heap[rci] < self.heap[min_child_index]:
            min_child_index = rci
        return min_child_index

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


def heap_sort(arr):
    min_heap = MinHeap()
    for i in arr:
        min_heap.insert(i)

    counter = 0
    while not min_heap.is_empty():
        arr[counter] = min_heap.pop()
        counter += 1


def sort_matrix(mtx):
    n, m = len(mtx), len(mtx[0])
    i_counter, j_counter = 0, 0
    sorted_mtx = [[None for _ in range(m)] for _ in range(n)]

    flattened_mtx = []
    for i in range(n):
        for j in range(m):
            flattened_mtx.append(mtx[i][j])

    heap_sort(flattened_mtx)
    for i in flattened_mtx:
        sorted_mtx[i_counter][j_counter] = i
        j_counter += 1
        if j_counter == m:
            j_counter = 0
            i_counter += 1

    return sorted_mtx


mtx1 = [[10, 20, 30, 40],
        [15, 25, 35, 45],
        [27, 29, 37, 48],
        [32, 33, 39, 50]]
sorted_mtx1 = sort_matrix(mtx1)
for i in sorted_mtx1:
    print(i)

mtx2 = [[1, 5, 3], [2, 8, 7], [4, 6, 9]]
sorted_mtx2 = sort_matrix(mtx2)
for i in sorted_mtx2:
    print(i)
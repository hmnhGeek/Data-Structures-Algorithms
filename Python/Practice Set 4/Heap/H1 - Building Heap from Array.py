# Problem link - https://www.geeksforgeeks.org/dsa/building-heap-from-array/


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


class MaxHeap:
    def __init__(self):
        self.heap = []

    def is_empty(self):
        return len(self.heap) == 0

    def get_lci(self, pi):
        ci = 2 * pi + 1
        if ci in range(len(self.heap)):
            return ci
        return None

    def get_rci(self, pi):
        ci = 2 * pi + 2
        if ci in range(len(self.heap)):
            return ci
        return None

    def get_pi(self, ci):
        pi = int((ci - 1) / 2)
        if pi in range(len(self.heap)):
            return pi
        return None

    def get_max_child_index(self, lci, rci):
        if lci is None and rci is None:
            return None
        if lci is None:
            return rci
        if rci is None:
            return lci
        max_child_index = lci
        if self.heap[rci] > self.heap[max_child_index]:
            max_child_index = rci
        return max_child_index

    def max_heapify_up(self, start_index):
        if start_index == 0:
            return
        pi = self.get_pi(start_index)
        lci, rci = self.get_lci(pi), self.get_rci(pi)
        max_child_index = self.get_max_child_index(lci, rci)
        if max_child_index is not None:
            if self.heap[pi] < self.heap[max_child_index]:
                swap(self.heap, pi, max_child_index)
            self.max_heapify_up(pi)

    def max_heapify_down(self, pi):
        lci, rci = self.get_lci(pi), self.get_rci(pi)
        max_child_index = self.get_max_child_index(lci, rci)
        if max_child_index is not None:
            if self.heap[pi] < self.heap[max_child_index]:
                swap(self.heap, pi, max_child_index)
            self.max_heapify_down(max_child_index)

    def insert(self, x):
        self.heap.append(x)
        self.max_heapify_up(len(self.heap) - 1)

    def pop(self):
        if self.is_empty():
            return
        item = self.heap[0]
        swap(self.heap, 0, -1)
        del self.heap[-1]
        self.max_heapify_down(0)
        return item


# Usage
h = MaxHeap()
for i in [1, 2, 4, 9, 6, 9, 8, 2, 3, 6]:
    h.insert(i)

while not h.is_empty():
    print(h.pop())

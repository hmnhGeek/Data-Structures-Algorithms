class MaxHeap:
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

    def get_max_child_index(self, lci, rci):
        if lci is None and rci is None:
            return
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
                self.heap[pi], self.heap[max_child_index] = self.heap[max_child_index], self.heap[pi]
            self.max_heapify_up(pi)

    def max_heapify_down(self, pi):
        lci, rci = self.get_lci(pi), self.get_rci(pi)
        max_child_index = self.get_max_child_index(lci, rci)
        if max_child_index is not None:
            if self.heap[pi] < self.heap[max_child_index]:
                self.heap[pi], self.heap[max_child_index] = self.heap[max_child_index], self.heap[pi]
            self.max_heapify_down(max_child_index)

    def insert(self, x):
        self.heap.append(x)
        self.max_heapify_up(len(self.heap) - 1)

    def top(self):
        if self.is_empty():
            return
        return self.heap[0]

    def pop(self):
        if self.is_empty():
            return
        item = self.heap[0]
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        del self.heap[-1]
        self.max_heapify_down(0)
        return item


class SlidingWindowMaximum:
    @staticmethod
    def get_max(arr, k):
        n = len(arr)
        if k > n:
            print(max(arr))
            return
        max_heap = MaxHeap()
        for i in range(k):
            max_heap.insert(arr[i])
        for i in range(n - k + 1):
            print(max_heap.top(), end=" ")
            if arr[i] == max_heap.top():
                max_heap.pop()
            if 0 <= i + k < n:
                max_heap.insert(arr[i + k])
        print()


SlidingWindowMaximum.get_max([1, 2, 3, 1, 4, 5], 3)
SlidingWindowMaximum.get_max([8, 5, 10, 7, 9, 4, 15, 12, 90, 13], 4)
SlidingWindowMaximum.get_max([20, 10, 30], 1)
SlidingWindowMaximum.get_max([1, 3, -1, -3, 5, 3, 6, 7], 3)

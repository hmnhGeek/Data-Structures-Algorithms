class MaxHeap:
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

    def get_max_child_index(self, lci, rci):
        if lci is None and rci is None:
            return
        if lci is None:
            return rci
        if rci is None:
            return lci
        max_child_index = lci
        if self.heap[rci][0] > self.heap[max_child_index][0]:
            max_child_index = rci
        return max_child_index

    def max_heapify_up(self, start_index):
        if start_index == 0:
            return
        pi = self.get_pi(start_index)
        lci, rci = self.get_lci(pi), self.get_rci(pi)
        max_child_index = self.get_max_child_index(lci, rci)
        if max_child_index is not None:
            if self.heap[pi][0] < self.heap[max_child_index][0]:
                self.heap[pi], self.heap[max_child_index] = self.heap[max_child_index], self.heap[pi]
            self.max_heapify_up(pi)

    def max_heapify_down(self, pi):
        lci, rci = self.get_lci(pi), self.get_rci(pi)
        max_child_index = self.get_max_child_index(lci, rci)
        if max_child_index is not None:
            if self.heap[pi][0] < self.heap[max_child_index][0]:
                self.heap[pi], self.heap[max_child_index] = self.heap[max_child_index], self.heap[pi]
            self.max_heapify_down(max_child_index)

    def insert(self, x):
        self.heap.append(x)
        self.max_heapify_up(len(self.heap) - 1)

    def pop(self):
        if self.is_empty():
            return
        item = self.heap[0]
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        del self.heap[-1]
        self.max_heapify_down(0)
        return item


class Solution:
    @staticmethod
    def sliding_window_maximum(arr, k):
        # edge case
        if k <= 0 or k > len(arr):
            return -1

        # define a max heap which can store at max `n` elements.
        max_heap = MaxHeap()
        result = []
        n = len(arr)

        for i in range(n):
            # push the current element into the max heap
            max_heap.insert((arr[i], i))

            # Remove elements outside the window
            while max_heap.heap[0][1] <= i - k:
                max_heap.pop()

            # Append current max to result once the first window is completed
            if i >= k - 1:
                result.append(max_heap.heap[0][0])
        return result


print(Solution.sliding_window_maximum([1, 2, 3, 1, 4, 5, 2, 3, 6], 3))
print(Solution.sliding_window_maximum([5, 1, 3, 4, 2, 6], 1))
print(Solution.sliding_window_maximum([1, 3, 2, 1, 7, 3], 3))
print(Solution.sliding_window_maximum([1, 3, -1, -3, 5, 3, 6, 7], 3))

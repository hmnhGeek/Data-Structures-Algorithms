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
    def minimize_distance(arr, k):
        if k <= 0:
            return
        n = len(arr)
        max_heap = MaxHeap()
        gas_stations_placed_tracker = {i: 0 for i in range(n - 1)}
        for i in range(n - 1):
            max_heap.insert((arr[i + 1] - arr[i], i))
        for i in range(k):
            distance, index = max_heap.pop()
            gas_stations_placed_tracker[index] += 1
            max_heap.insert(
                (
                    (arr[index + 1] - arr[index])/(gas_stations_placed_tracker[index] + 1),
                    index
                )
            )
        return max_heap.heap[0][0]


print(Solution.minimize_distance([1, 2, 3, 4, 5, 6, 7], 6))
print(Solution.minimize_distance([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1))
print(Solution.minimize_distance([3, 6, 12, 19, 33, 44, 67, 72, 89, 95], 2))
print(Solution.minimize_distance([1, 13, 17, 23], 5))

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
    def place_gas_stations(arr, k):
        n = len(arr)
        slots = [0]*(n - 1)
        max_heap = MaxHeap()
        for i in range(n - 1):
            max_heap.insert((arr[i + 1] - arr[i], i))
        for i in range(k):
            updated_slot_length, index = max_heap.pop()
            initial_length = (slots[index] + 1) * updated_slot_length
            new_length = initial_length/(slots[index] + 1 + 1)
            slots[index] += 1
            max_heap.insert((new_length, index))
        max_min_length, _ = max_heap.pop()
        return max_min_length


print(Solution.place_gas_stations([1,2,3,4,5,6,7], 6))
print(Solution.place_gas_stations([1, 2, 3, 4, 5], 4))
print(Solution.place_gas_stations(list(range(1, 11)), 1))
print(Solution.place_gas_stations([3, 6, 12, 19, 33, 44, 67, 72, 89, 95], 2))
print(Solution.place_gas_stations([1, 13, 17, 23], 5))

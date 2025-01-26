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
    def get_smallest_range(lists):
        pq = MinHeap()
        max_elem = -1e6
        min_range = [-1e6, 1e6]
        for i in range(len(lists)):
            pq.insert((lists[i][0], i, 0))
            max_elem = max(max_elem, lists[i][0])
        while not pq.is_empty():
            min_elem, list_idx, index = pq.pop()
            updated_range = [min_elem, max_elem]
            if updated_range[1] - updated_range[0] == min_range[1] - min_range[0]:
                if min_elem < min_range[0]:
                    min_range = [min_elem, max_elem]
            elif updated_range[1] - updated_range[0] < min_range[1] - min_range[0]:
                min_range = updated_range
            if index + 1 < len(lists[list_idx]):
                max_elem = max(max_elem, lists[list_idx][index + 1])
                pq.insert((lists[list_idx][index + 1], list_idx, index + 1))
            else:
                break
        return min_range


print(
    Solution.get_smallest_range(
        [
            [1, 3, 5, 7, 9],
            [0, 2, 4, 6, 8],
            [2, 3, 5, 7, 11]
        ]
    )
)

print(
    Solution.get_smallest_range(
        [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12]
        ]
    )
)

print(Solution.get_smallest_range([[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]))
print(Solution.get_smallest_range([[1, 2, 3], [1, 2, 3], [1, 2, 3]]))

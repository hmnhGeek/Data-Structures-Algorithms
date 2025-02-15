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
        mci = self.get_min_child_index(lci, rci)
        if mci is not None:
            if self.heap[pi] > self.heap[mci]:
                self.heap[pi], self.heap[mci] = self.heap[mci], self.heap[pi]
            self.min_heapify_up(pi)

    def min_heapify_down(self, pi):
        lci, rci = self.get_lci(pi), self.get_rci(pi)
        mci = self.get_min_child_index(lci, rci)
        if mci is not None:
            if self.heap[pi] > self.heap[mci]:
                self.heap[pi], self.heap[mci] = self.heap[mci], self.heap[pi]
            self.min_heapify_down(mci)

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

    def __len__(self):
        return len(self.heap)

    def top(self):
        if self.is_empty():
            return None
        return self.heap[0]


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

    def min_heapify_up(self, start_index):
        if start_index == 0:
            return
        pi = self.get_pi(start_index)
        lci, rci = self.get_lci(pi), self.get_rci(pi)
        mci = self.get_max_child_index(lci, rci)
        if mci is not None:
            if self.heap[pi] < self.heap[mci]:
                self.heap[pi], self.heap[mci] = self.heap[mci], self.heap[pi]
            self.min_heapify_up(pi)

    def min_heapify_down(self, pi):
        lci, rci = self.get_lci(pi), self.get_rci(pi)
        mci = self.get_max_child_index(lci, rci)
        if mci is not None:
            if self.heap[pi] < self.heap[mci]:
                self.heap[pi], self.heap[mci] = self.heap[mci], self.heap[pi]
            self.min_heapify_down(mci)

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

    def __len__(self):
        return len(self.heap)

    def top(self):
        if self.is_empty():
            return None
        return self.heap[0]


class Solution:
    @staticmethod
    def median_finder(stream):
        min_heap, max_heap = MinHeap(), MaxHeap()
        result = []
        for i in range(len(stream)):
            elem = stream[i]
            if max_heap.is_empty():
                max_heap.insert(elem)
            elif max_heap.top() <= elem:
                min_heap.insert(elem)
            else:
                max_heap.insert(elem)
            if len(max_heap) - len(min_heap) == 0:
                pass
            elif len(max_heap) - len(min_heap) == 1:
                pass
            elif len(max_heap) - len(min_heap) > 1:
                min_heap.insert(max_heap.pop())
            else:
                max_heap.insert(min_heap.pop())
            if (len(max_heap) + len(min_heap)) % 2 == 0:
                result.append((max_heap.top() + min_heap.top()) / 2)
            else:
                result.append(max_heap.top())
        return result


print(Solution.median_finder([5, 15, 1, 3, 7]))
print(Solution.median_finder([5, 10, 15]))
print(Solution.median_finder([2, 1, 7, 8, 5, 8, 4]))

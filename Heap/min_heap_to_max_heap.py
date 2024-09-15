class Heap:
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
            return None
        pi = int((ci - 1)/2)
        return pi if pi in range(len(self.heap)) else None

    def get_min_child_index(self, lci, rci):
        if lci is None and rci is None:
            return None
        if lci is None:
            return rci
        if rci is None:
            return lci
        min_child_index = lci
        if self.heap[rci] < self.heap[min_child_index]:
            min_child_index = rci
        return min_child_index

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

    def heapify_up(self, start_index):
        pass

    def heapify_down(self, pi):
        pass

    def insert(self, x):
        self.heap.append(x)
        self.heapify_up(len(self.heap) - 1)

    def pop(self):
        if len(self.heap) == 0:
            return
        item = self.heap[0]
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        del self.heap[-1]
        self.heapify_down(0)
        return item


class MinHeap(Heap):
    def __init__(self):
        super().__init__()

    def heapify_up(self, start_index):
        if start_index == 0:
            return
        pi = self.get_pi(start_index)
        lci, rci = self.get_lci(pi), self.get_rci(pi)
        min_child_index = self.get_min_child_index(lci, rci)

        if min_child_index is not None:
            if self.heap[pi] > self.heap[min_child_index]:
                self.heap[pi], self.heap[min_child_index] = self.heap[min_child_index], self.heap[pi]
            self.heapify_up(pi)

    def heapify_down(self, pi):
        lci, rci = self.get_lci(pi), self.get_rci(pi)
        min_child_index = self.get_min_child_index(lci, rci)

        if min_child_index is not None:
            if self.heap[pi] > self.heap[min_child_index]:
                self.heap[pi], self.heap[min_child_index] = self.heap[min_child_index], self.heap[pi]
            self.heapify_down(min_child_index)


class MaxHeap(Heap):
    def __init__(self):
        super().__init__()

    def heapify_up(self, start_index):
        if start_index == 0:
            return
        pi = self.get_pi(start_index)
        lci, rci = self.get_lci(pi), self.get_rci(pi)
        max_child_index = self.get_max_child_index(lci, rci)

        if max_child_index is not None:
            if self.heap[pi] < self.heap[max_child_index]:
                self.heap[pi], self.heap[max_child_index] = self.heap[max_child_index], self.heap[pi]
            self.heapify_up(pi)

    def heapify_down(self, pi):
        lci, rci = self.get_lci(pi), self.get_rci(pi)
        max_child_index = self.get_max_child_index(lci, rci)

        if max_child_index is not None:
            if self.heap[pi] < self.heap[max_child_index]:
                self.heap[pi], self.heap[max_child_index] = self.heap[max_child_index], self.heap[pi]
            self.heapify_down(max_child_index)


def show_heap(h):
    while not h.is_empty():
        print(h.pop())


def convert_min_to_max_heap(min_heap: MinHeap) -> MaxHeap:
    max_heap = MaxHeap()
    while not min_heap.is_empty():
        max_heap.insert(min_heap.pop())
    return max_heap


# Example 1
l1 = [3, 5, 9, 6, 8, 20, 10, 12, 18, 9]
h1 = MinHeap()
for i in l1:
    h1.insert(i)
h2 = convert_min_to_max_heap(h1)
show_heap(h2)
print()

# Example 2
l2 = [3, 4, 8, 11, 13]
h1 = MinHeap()
for i in l2:
    h1.insert(i)
h2 = convert_min_to_max_heap(h1)
show_heap(h2)
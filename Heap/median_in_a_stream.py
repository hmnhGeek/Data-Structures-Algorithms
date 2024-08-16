from abc import ABC, abstractmethod


class Heap(ABC):
    def __init__(self):
        self.heap = []

    def is_empty(self):
        return len(self.heap) == 0

    def get_top(self):
        return self.heap[0] if not self.is_empty() else None

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

    def _get_min_child_index(self, lci, rci):
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

    def _get_max_child_index(self, lci, rci):
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

    @abstractmethod
    def heapify_up(self, start_index):
        pass

    @abstractmethod
    def heapify_down(self, pi):
        pass

    @abstractmethod
    def insert(self, x):
        pass

    @abstractmethod
    def pop(self):
        pass


class MinHeap(Heap):
    def __init__(self):
        super().__init__()

    def heapify_up(self, start_index):
        if start_index == 0:
            return

        pi = self.get_pi(start_index)
        lci, rci = self.get_lci(pi), self.get_rci(pi)
        min_child_index = self._get_min_child_index(lci, rci)

        if min_child_index is not None:
            if self.heap[pi] > self.heap[min_child_index]:
                self.heap[pi], self.heap[min_child_index] = self.heap[min_child_index], self.heap[pi]
            self.heapify_up(pi)

    def heapify_down(self, pi):
        lci, rci = self.get_lci(pi), self.get_rci(pi)
        min_child_index = self._get_min_child_index(lci, rci)

        if min_child_index is not None:
            if self.heap[pi] > self.heap[min_child_index]:
                self.heap[pi], self.heap[min_child_index] = self.heap[min_child_index], self.heap[pi]
            self.heapify_down(min_child_index)

    def insert(self, x):
        self.heap.append(x)
        self.heapify_up(len(self.heap) - 1)

    def pop(self):
        if self.is_empty():
            return

        item = self.heap[0]
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        del self.heap[-1]
        self.heapify_down(0)
        return item


class MaxHeap(Heap):
    def __init__(self):
        super().__init__()

    def heapify_up(self, start_index):
        if start_index == 0:
            return

        pi = self.get_pi(start_index)
        lci, rci = self.get_lci(pi), self.get_rci(pi)
        max_child_index = self._get_max_child_index(lci, rci)

        if max_child_index is not None:
            if self.heap[pi] < self.heap[max_child_index]:
                self.heap[pi], self.heap[max_child_index] = self.heap[max_child_index], self.heap[pi]
            self.heapify_up(pi)

    def heapify_down(self, pi):
        lci, rci = self.get_lci(pi), self.get_rci(pi)
        max_child_index = self._get_max_child_index(lci, rci)

        if max_child_index is not None:
            if self.heap[pi] < self.heap[max_child_index]:
                self.heap[pi], self.heap[max_child_index] = self.heap[max_child_index], self.heap[pi]
            self.heapify_down(max_child_index)

    def insert(self, x):
        self.heap.append(x)
        self.heapify_up(len(self.heap) - 1)

    def pop(self):
        if self.is_empty():
            return

        item = self.heap[0]
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        del self.heap[-1]
        self.heapify_down(0)
        return item


class DataStreamMedianFinder:
    def __init__(self):
        self.min_heap = MinHeap()
        self.max_heap = MaxHeap()

    def _get_stream_size(self):
        return len(self.min_heap.heap) + len(self.max_heap.heap)

    def _is_size_even(self):
        return self._get_stream_size() % 2 == 0

    def _heaps_have_equal_size(self):
        return len(self.min_heap.heap) == len(self.max_heap.heap)

    def _skewed_to_max_by_one_unit(self):
        return len(self.min_heap.heap) + 1 == len(self.max_heap.heap)

    def _highly_skewed_to_max(self):
        return len(self.max_heap.heap) > len(self.min_heap.heap) + 1

    def _balance_heaps(self):
        if self._heaps_have_equal_size() or self._skewed_to_max_by_one_unit():
            return

        if self._highly_skewed_to_max():
            self.min_heap.insert(self.max_heap.pop())
        else:
            self.max_heap.insert(self.min_heap.pop())

    def insert_in_stream(self, x):
        top_of_max_heap = self.max_heap.get_top()

        if top_of_max_heap is not None:
            if x > top_of_max_heap:
                self.min_heap.insert(x)
            else:
                self.max_heap.insert(x)
        else:
            self.max_heap.insert(x)

        self._balance_heaps()

    def get_median(self):
        if self._is_size_even():
            left_top = self.max_heap.get_top()
            right_top = self.min_heap.get_top()
            return (left_top + right_top)/2
        return self.max_heap.get_top()


def test_data_stream_median_finder(stream):
    data_stream_median_finder = DataStreamMedianFinder()
    for i in stream:
        print(f"Inserting {i} into the data stream.")
        data_stream_median_finder.insert_in_stream(i)
        print(f"Median at this point is {data_stream_median_finder.get_median()}")


test_data_stream_median_finder([5, 15, 1, 3])
print()
test_data_stream_median_finder([5, 10, 15])
print()
test_data_stream_median_finder([2, 3, 4])
print()
test_data_stream_median_finder([1, 2, 3])
print()
test_data_stream_median_finder([2, 2, 2, 2])

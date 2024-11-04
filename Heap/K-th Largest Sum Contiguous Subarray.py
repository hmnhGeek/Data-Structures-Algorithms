# Problem link - https://www.geeksforgeeks.org/k-th-largest-sum-contiguous-subarray/


class MaxHeap:
    def __init__(self):
        self.heap = []

    def get_lci(self, pi):
        if pi is None: return
        lci = 2 * pi + 1
        return lci if lci in range(len(self.heap)) else None

    def get_rci(self, pi):
        if pi is None: return
        rci = 2 * pi + 2
        return rci if rci in range(len(self.heap)) else None

    def get_pi(self, ci):
        if ci == 0: return
        pi = int((ci - 1) / 2)
        return pi if pi in range(len(self.heap)) else None

    def get_max_child(self, lci, rci):
        if lci is None and rci is None: return None
        if lci is None: return rci
        if rci is None: return lci

        max_child_index = lci
        if self.heap[rci] > self.heap[max_child_index]:
            max_child_index = rci

        return max_child_index

    def max_heapify_up(self, start_index):
        if start_index == 0: return

        pi = self.get_pi(start_index)
        lci, rci = self.get_lci(pi), self.get_rci(pi)
        max_child_index = self.get_max_child(lci, rci)

        if max_child_index is not None:
            if self.heap[pi] < self.heap[max_child_index]:
                self.heap[pi], self.heap[max_child_index] = self.heap[max_child_index], self.heap[pi]
            self.max_heapify_up(pi)

    def max_heapify_down(self, pi):
        lci, rci = self.get_lci(pi), self.get_rci(pi)
        max_child_index = self.get_max_child(lci, rci)

        if max_child_index is not None:
            if self.heap[pi] < self.heap[max_child_index]:
                self.heap[pi], self.heap[max_child_index] = self.heap[max_child_index], self.heap[pi]
            self.max_heapify_down(max_child_index)

    def insert(self, x):
        self.heap.append(x)
        self.max_heapify_up(len(self.heap) - 1)

    def pop(self):
        if len(self.heap) == 0: return
        item = self.heap[0]
        li = len(self.heap) - 1
        self.heap[0], self.heap[li] = self.heap[li], self.heap[0]
        del self.heap[li]
        self.max_heapify_down(0)
        return item


def kth_largest_contiguous_sum(arr, k):
    h = MaxHeap()
    for i in range(len(arr)):
        s = 0
        for j in range(i, len(arr)):
            s += arr[j]
            h.insert(s)
    counter = 0
    while counter != k - 1:
        h.pop()
        counter += 1
    return h.pop()


print(kth_largest_contiguous_sum([20, -5, -1], 3))
print(kth_largest_contiguous_sum([10, -10, 20, -40], 6))
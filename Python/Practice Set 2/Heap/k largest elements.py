# Problem link - https://www.geeksforgeeks.org/problems/k-largest-elements4206/1


class MinHeap:
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
        min_child_index = self.get_min_child_index(lci, rci)
        if min_child_index is not None:
            if self.heap[pi] > self.heap[min_child_index]:
                self.heap[min_child_index], self.heap[pi] = self.heap[pi], self.heap[min_child_index]
            self.min_heapify_up(pi)

    def min_heapify_down(self, pi):
        lci, rci = self.get_lci(pi), self.get_rci(pi)
        min_child_index = self.get_min_child_index(lci, rci)
        if min_child_index is not None:
            if self.heap[pi] > self.heap[min_child_index]:
                self.heap[min_child_index], self.heap[pi] = self.heap[pi], self.heap[min_child_index]
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
    def get_k_largest(arr, k):
        """
            Time complexity is O(n * log(k)) time and space complexity is O(k).
        """

        # define a min heap and push first k elements into it in O(k * log(k)) time and O(k) space.
        min_heap = MinHeap()
        for i in range(k):
            min_heap.insert(arr[i])

        # iterate over the remaining elements in O({n - k} * log(k)) time
        i = k
        while i < len(arr):
            element = arr[i]
            if element > min_heap.heap[0]:
                min_heap.pop()
                min_heap.insert(element)
            i += 1
        return min_heap.heap


print(Solution.get_k_largest([12, 5, 787, 1, 23], 2))
print(Solution.get_k_largest([1, 23, 12, 9, 30, 2, 50], 3))
print(Solution.get_k_largest([12, 23], 1))
print(Solution.get_k_largest([11, 5, 12, 9, 44, 17, 2], 2))
print(Solution.get_k_largest([11, 3, 4, 6], 3))

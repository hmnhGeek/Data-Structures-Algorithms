# Problem link - https://www.geeksforgeeks.org/problems/merge-two-binary-max-heap0144/1


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
    def merge_max_heaps(h1: MaxHeap, h2: MaxHeap):
        """
            Overall time complexity is O({n + m} * log(n + m)) and space complexity is O(n + m).
        """

        # This heap will store n + m items.
        result = MaxHeap()

        # this will take O(n * {log(n + m) + log(n)}) time
        while not h1.is_empty():
            result.insert(h1.pop())

        # This will take O(m * {log(n + m) + log(m)}) time
        while not h2.is_empty():
            result.insert(h2.pop())

        # return the merged heap
        return result


# Example 1
h1 = MaxHeap()
for i in [10, 5, 6, 2]:
    h1.insert(i)
h2 = MaxHeap()
for i in [12, 7, 9]:
    h2.insert(i)
h = Solution.merge_max_heaps(h1, h2)
while not h.is_empty():
    print(h.pop(), end=" ")
print()

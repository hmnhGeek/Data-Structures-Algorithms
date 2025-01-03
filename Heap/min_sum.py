# Problem link - https://www.geeksforgeeks.org/problems/minimum-sum4058/1


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
    def get_min_sum(arr):
        """
            Time complexity is O(n*log(n)) and space complexity is O(n).
        """

        # store the numbers in n and m
        n, m = 0, 0
        pow = 0
        h = MaxHeap()

        # push the array elements into max heap in O(n*log(n)) time.
        for i in arr:
            h.insert(i)

        # while the heap is not empty. We use max heap to assign LSB with highest value.
        while not h.is_empty():
            # construct `n`
            a = h.pop()
            n += (a * 10**pow) if a is not None else 0

            # construct `m`
            b = h.pop()
            m += (b * 10**pow) if b is not None else 0

            # increment power `pow`
            pow += 1

        # return the sum of the numbers
        return n + m


print(Solution.get_min_sum([6, 8, 4, 5, 2, 3]))
print(Solution.get_min_sum([5, 3, 0, 7, 4]))
print(Solution.get_min_sum([9, 4]))

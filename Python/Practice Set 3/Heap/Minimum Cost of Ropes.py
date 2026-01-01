# Problem link - https://www.geeksforgeeks.org/problems/minimum-cost-of-ropes-1587115620/1


class MinHeap:
    def __init__(self):
        self.heap = []

    def is_empty(self):
        return len(self.heap) == 0

    def get_lci(self, pi):
        lci = 2*pi + 1
        if 0 <= lci < len(self.heap):
            return lci
        return None

    def get_rci(self, pi):
        rci = 2*pi + 2
        if 0 <= rci < len(self.heap):
            return rci
        return None

    def get_pi(self, ci):
        if ci == 0:
            return
        pi = int((ci - 1)/2)
        if 0 <= pi < len(self.heap):
            return pi
        return None

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
                self.heap[pi], self.heap[min_child_index] = self.heap[min_child_index], self.heap[pi]
            self.min_heapify_up(pi)

    def min_heapify_down(self, pi):
        lci, rci = self.get_lci(pi), self.get_rci(pi)
        min_child_index = self.get_min_child_index(lci, rci)
        if min_child_index is not None:
            if self.heap[pi] > self.heap[min_child_index]:
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
    def get_min_cost(ropes):
        """
            Time complexity is O(n * log(n)) and space complexity is O(n).
        """
        pq = MinHeap()
        for i in ropes:
            pq.insert(i)
        cost = 0
        while len(pq.heap) != 1:
            a, b = pq.pop(), pq.pop()
            cost += (a + b)
            pq.insert(a + b)
        return cost


print(Solution.get_min_cost([4, 3, 2, 6]))
print(Solution.get_min_cost([4, 2, 7, 6, 9]))
print(Solution.get_min_cost([10]))
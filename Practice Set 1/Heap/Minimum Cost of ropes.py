# Problem link - https://www.geeksforgeeks.org/problems/minimum-cost-of-ropes-1587115620/1


from typing import List


class MinHeap:
    def __init__(self):
        self.heap = []

    def is_empty(self):
        return len(self.heap) == 0

    def get_lci(self, pi):
        lci = 2*pi + 1
        return lci if lci in range(len(self.heap)) else None

    def get_rci(self, pi):
        rci = 2 * pi + 2
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
    def min_cost_of_ropes(ropes: List[int]) -> int:
        """
            Overall time complexity is O(n*log(n)) and space complexity is O(n) for the min heap.
        """

        # construct a min heap and a min cost variable.
        min_heap = MinHeap()
        min_cost = 0

        # push all the ropes into the heap in O(n*log(n)) time.
        for i in ropes:
            min_heap.insert(i)

        # This should run for n times approximately, i.e., O(n * 3 * log(n))
        while not len(min_heap.heap) == 1:
            # get the cost of connecting two shortest length ropes, in O(2*log(n)) time.
            cost = min_heap.pop() + min_heap.pop()
            # add this cost in min_cost.
            min_cost += cost
            # insert the current cost back to the min heap in O(log(n)) time.
            min_heap.insert(cost)

        # return the min cost obtained.
        return min_cost


print(Solution.min_cost_of_ropes([4, 3, 2, 6]))
print(Solution.min_cost_of_ropes([4, 2, 7, 6, 9]))
print(Solution.min_cost_of_ropes([10]))
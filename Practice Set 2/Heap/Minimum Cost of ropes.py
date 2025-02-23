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
    def min_cost(arr):
        """
            Time complexity is O(n * log(n)) and space complexity is O(n).
        """

        # create a min heap and push all the elements from the array into it in O(n * log(n)) time and O(n) space.
        pq = MinHeap()
        for i in arr:
            pq.insert(i)

        # initialize a cost variable to store the total cost of connecting the ropes.
        cost = 0

        # while there are more than 1 ropes in the heap to connect. This shall run of `n` times.
        while not pq.is_empty() and len(pq.heap) > 1:
            # get the two shortest ropes and add their cost.
            a, b = pq.pop(), pq.pop()
            cost += a + b

            # if the heap still has some ropes left, push back the connected rope into it in log(n) time.
            if not pq.is_empty():
                pq.insert(a + b)

        # return the final minimum cost of connecting all the ropes.
        return cost


print(Solution.min_cost([4, 3, 2, 6]))
print(Solution.min_cost([4, 2, 7, 6, 9]))
print(Solution.min_cost([10]))
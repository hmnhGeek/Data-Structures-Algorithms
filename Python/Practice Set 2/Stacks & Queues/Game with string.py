# Problem link - https://www.geeksforgeeks.org/problems/game-with-string4100/1


from collections import Counter


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
        if self.heap[rci][0] > self.heap[max_child_index][0]:
            max_child_index = rci
        return max_child_index

    def max_heapify_up(self, start_index):
        if start_index == 0:
            return
        pi = self.get_pi(start_index)
        lci, rci = self.get_lci(pi), self.get_rci(pi)
        max_child_index = self.get_max_child_index(lci, rci)
        if max_child_index is not None:
            if self.heap[pi][0] < self.heap[max_child_index][0]:
                self.heap[pi], self.heap[max_child_index] = self.heap[max_child_index], self.heap[pi]
            self.max_heapify_up(pi)

    def max_heapify_down(self, pi):
        lci, rci = self.get_lci(pi), self.get_rci(pi)
        max_child_index = self.get_max_child_index(lci, rci)
        if max_child_index is not None:
            if self.heap[pi][0] < self.heap[max_child_index][0]:
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
    def game_with_string(string, k):
        """
            Time complexity is O({n + k} * log(n)) and space complexity is O(n).
        """

        # edge case
        if k < 0 or k > len(string):
            return -1

        # push frequencies of characters into the max heap in O(n * log(n)) time and O(n) space.
        d = dict(Counter(string))
        max_heap = MaxHeap()
        for key, val in d.items():
            max_heap.insert((val, key))

        # initialize a counter to track k-removals.
        counter = 0

        # This loop will run for k times, i.e., O(k * log(n)) time.
        while counter != k:
            freq, character = max_heap.pop()
            counter += 1
            if freq - 1 >= 0:
                max_heap.insert((freq - 1, character))

        # calculate the result value in O(n * log(n)) time.
        result = 0
        while not max_heap.is_empty():
            freq, _ = max_heap.pop()
            result += freq**2
        return result


print(Solution.game_with_string("abccc", 1))
print(Solution.game_with_string("aabcbcbcabcc", 3))
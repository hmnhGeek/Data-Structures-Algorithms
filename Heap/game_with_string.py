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
            return None
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

    def push(self, x):
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
    def game_with_string(string: str, k: int) -> int:
        """
            Overall time complexity is O(n*log(n)) and space complexity is O(n).
        """

        # if you want to remove all the characters from the string or more than those, return 0.
        if k >= len(string):
            return 0

        # get the frequencies of each character as a list. No need for characters, we just want distinct frequencies.
        # This will take O(n) time and O(n) space in worst case when all characters are unique.
        frequencies = list(dict(Counter(string)).values())

        # initialize a max heap to always get the max frequency in O(log(n)) time.
        max_heap = MaxHeap()
        # push the frequencies into the max heap. This will occupy O(n) space in worst case.
        for frequency in frequencies:
            max_heap.push(frequency)

        # initialize a counter = k, so as not to modify actual `k` value.
        counter = k

        # since counter < len(string), heap will always contain data even if counter becomes 0.
        # This will take O(k*log(n)) time.
        while counter != 0:
            # pop the highest frequency
            max_freq = max_heap.pop()

            # decrement it and also decrement the counter, which means we have removed a character.
            max_freq -= 1
            counter -= 1

            # if max_freq is still greater than 0, push it back to heap.
            if max_freq > 0:
                max_heap.push(max_freq)

        # once counter turns 0, i.e., all the `k` characters have been removed, start popping the leftover
        # frequencies from the max heap. This will again take O(n*log(n)) time.
        result = 0
        while not max_heap.is_empty():
            # add these frequencies by squaring them into the result.
            result += (max_heap.pop())**2

        # finally return the result.
        return result


print(Solution.game_with_string("abccc", 1))
print(Solution.game_with_string("aabcbcbcabcc", 3))
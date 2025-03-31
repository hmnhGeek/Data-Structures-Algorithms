# Problem link - https://www.geeksforgeeks.org/problems/rearrange-characters4649/1


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
        if self.heap[rci][1] > self.heap[max_child_index][1]:
            max_child_index = rci
        return max_child_index

    def max_heapify_up(self, start_index):
        if start_index == 0:
            return
        pi = self.get_pi(start_index)
        lci, rci = self.get_lci(pi), self.get_rci(pi)
        max_child_index = self.get_max_child_index(lci, rci)
        if max_child_index is not None:
            if self.heap[pi][1] < self.heap[max_child_index][1]:
                self.heap[pi], self.heap[max_child_index] = self.heap[max_child_index], self.heap[pi]
            self.max_heapify_up(pi)

    def max_heapify_down(self, pi):
        lci, rci = self.get_lci(pi), self.get_rci(pi)
        max_child_index = self.get_max_child_index(lci, rci)
        if max_child_index is not None:
            if self.heap[pi][1] < self.heap[max_child_index][1]:
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
    def rearrange_characters(string):
        """
            Overall time complexity is O(n*log(n)) and space complexity is O(n).
        """

        max_heap = MaxHeap()

        # push all the frequencies into the max heap in O(n*log(n)) time.
        d = dict(Counter(string))
        for item in d.items():
            max_heap.insert(item)

        # run this algorithm till the max heap does not get empty.
        prev = None
        result = ""
        # overall this runs for O(n*log(n)) time
        while not max_heap.is_empty():
            # pop in O(log(n)) time.
            char, freq = max_heap.pop()
            result += char
            if prev and prev[1] > 0:
                # insert in log(n) time.
                max_heap.insert(prev)
            prev = (char, freq - 1)
        return result if prev[1] == 0 else ""


print(Solution.rearrange_characters("book"))
print(Solution.rearrange_characters("geeksforgeeks"))
print(Solution.rearrange_characters("address"))
print(Solution.rearrange_characters("mississippi"))
print(Solution.rearrange_characters("aaaa"))
print(Solution.rearrange_characters("bbbbbb"))
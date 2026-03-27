# Problem link - https://www.geeksforgeeks.org/rearrange-characters-string-no-two-adjacent/


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


class HeapElement:
    def __init__(self, character, count):
        self.character = character
        self.count = count

    def __lt__(self, other):
        return self.count < other.count

    def __gt__(self, other):
        return self.count > other.count


class Solution:
    @staticmethod
    def reorganize_string(string):
        """
            Time complexity is O(n * log(n)) and space complexity is O(n).
        """
        d = dict(Counter(string))
        max_heap = MaxHeap()
        for k, v in d.items():
            max_heap.insert(HeapElement(k, v))
        prev = None
        result = ""
        while not max_heap.is_empty():
            heapElement = max_heap.pop()
            character, count = heapElement.character, heapElement.count
            if prev is not None and prev.count > 0:
                max_heap.insert(HeapElement(prev.character, prev.count))
            result += character
            prev = HeapElement(character, count - 1)
        if prev is not None and prev.count > 0:
            return ""
        return result


print(Solution.reorganize_string("aab"))
print(Solution.reorganize_string("aaab"))
print(Solution.reorganize_string("address"))
print(Solution.reorganize_string("mississippi"))
print(Solution.reorganize_string("aaabc"))
print(Solution.reorganize_string("aaabb"))
print(Solution.reorganize_string("aa"))
print(Solution.reorganize_string("aaaabc"))
print(Solution.reorganize_string("abaab"))
print(Solution.reorganize_string("bbbbbb"))

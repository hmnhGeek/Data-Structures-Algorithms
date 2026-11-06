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
            return None
        if lci is None:
            return rci
        if rci is None:
            return lci
        mci = lci
        if self.heap[rci] > self.heap[mci]:
            mci = rci
        return mci

    def max_heapify_up(self, start_index):
        if start_index == 0:
            return
        pi = self.get_pi(start_index)
        lci, rci = self.get_lci(pi), self.get_rci(pi)
        mci = self.get_max_child_index(lci, rci)
        if mci is not None:
            if self.heap[pi] < self.heap[mci]:
                self.heap[mci], self.heap[pi] = self.heap[pi], self.heap[mci]
            self.max_heapify_up(pi)

    def max_heapify_down(self, pi):
        lci, rci = self.get_lci(pi), self.get_rci(pi)
        mci = self.get_max_child_index(lci, rci)
        if mci is not None:
            if self.heap[pi] < self.heap[mci]:
                self.heap[mci], self.heap[pi] = self.heap[pi], self.heap[mci]
            self.max_heapify_down(mci)

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
    def reorganize_string(string: str) -> str:
        """
            Time complexity is O(n * log(n)) and space complexity is O(n).
        """

        max_heap = MaxHeap()
        prev = None
        result = ""
        Solution._initiate_heap(max_heap, string)

        # This will run for n-iterations and thus, takes O(n * log(n)) time.
        while not max_heap.is_empty():
            heap_element = max_heap.pop()
            character, freq = heap_element.character, heap_element.count
            result += character
            if prev is not None:
                max_heap.insert(prev)
                prev = None
            if freq - 1 > 0:
                prev = HeapElement(character, freq - 1)
        if prev is not None:
            return ""
        return result

    @staticmethod
    def _initiate_heap(max_heap, string):
        """
            Time: O(n * log(n)) and Space: O(n).
        """
        d = dict(Counter(string))
        for key, val in d.items():
            max_heap.insert(HeapElement(key, val))


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

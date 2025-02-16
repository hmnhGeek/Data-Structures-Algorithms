# Problem link - https://www.geeksforgeeks.org/problems/merge-k-sorted-arrays/1


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
        if self.heap[rci][0] < self.heap[min_child_index][0]:
            min_child_index = rci
        return min_child_index

    def min_heapify_up(self, start_index):
        if start_index == 0:
            return
        pi = self.get_pi(start_index)
        lci, rci = self.get_lci(pi), self.get_rci(pi)
        min_child_index = self.get_min_child_index(lci, rci)
        if min_child_index is not None:
            if self.heap[pi][0] > self.heap[min_child_index][0]:
                self.heap[pi], self.heap[min_child_index] = self.heap[min_child_index], self.heap[pi]
            self.min_heapify_up(pi)

    def min_heapify_down(self, pi):
        lci, rci = self.get_lci(pi), self.get_rci(pi)
        min_child_index = self.get_min_child_index(lci, rci)
        if min_child_index is not None:
            if self.heap[pi][0] > self.heap[min_child_index][0]:
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
    def merge_k_sorted_lists(lists):
        """
            Overall time complexity is O(n*log(k)) and space complexity is O(k).
        """

        min_heap = MinHeap()
        result = []

        # This will take O(k*log(k)) where k is the number of lists
        for i in range(len(lists)):
            if len(lists[i]) > 0:
                min_heap.insert((lists[i][0], i, 0))

        # This will store n nodes in worst case
        while not min_heap.is_empty():
            # this will take O(log(k))
            item, x, y = min_heap.pop()
            result.append(item)

            # Another O(log(k))
            if 0 <= y + 1 < len(lists[x]):
                min_heap.insert((lists[x][y + 1], x, y + 1))

        return result


print(
    Solution.merge_k_sorted_lists(
        [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
    )
)

print(
    Solution.merge_k_sorted_lists(
        [
            [1, 4, 5],
            [1, 3, 4],
            [2, 6]
        ]
    )
)

print(
    Solution.merge_k_sorted_lists([])
)

print(
    Solution.merge_k_sorted_lists([[]])
)

print(
    Solution.merge_k_sorted_lists(
        [
            [1],
            [2, 4],
            [3, 7, 9, 11],
            [13]
        ]
    )
)
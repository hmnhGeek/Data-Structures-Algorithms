# Problem link - https://www.geeksforgeeks.org/problems/find-smallest-range-containing-elements-from-k-lists/1
# Solution - https://www.youtube.com/watch?v=0IqFMBatlhU


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
            return None
        pi = int((ci - 1)/2)
        return pi if pi in range(len(self.heap)) else None

    def get_min_child_index(self, lci, rci):
        if lci is None and rci is None:
            return None
        if lci is None:
            return rci
        if rci is None:
            return lci
        mci = lci
        if self.heap[rci] < self.heap[mci]:
            mci = rci
        return mci

    def min_heapify_up(self, start_index):
        if start_index == 0:
            return
        pi = self.get_pi(start_index)
        lci, rci = self.get_lci(pi), self.get_rci(pi)
        mci = self.get_min_child_index(lci, rci)
        if mci is not None:
            if self.heap[pi] > self.heap[mci]:
                self.heap[pi], self.heap[mci] = self.heap[mci], self.heap[pi]
            self.min_heapify_up(pi)

    def min_heapify_down(self, pi):
        lci, rci = self.get_lci(pi), self.get_rci(pi)
        mci = self.get_min_child_index(lci, rci)
        if mci is not None:
            if self.heap[pi] > self.heap[mci]:
                self.heap[pi], self.heap[mci] = self.heap[mci], self.heap[pi]
            self.min_heapify_down(mci)

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
    def get_smallest_range(mtx):
        """
            Time complexity is O(n * log(k)) and space complexity is O(k).
        """
        n = len(mtx)
        pq = MinHeap()
        mi, ma = 1e6, -1e6
        for i in range(n):
            l = mtx[i]
            mi = min(mi, l[0])
            ma = max(ma, l[0])
            pq.insert((l[0], i, 0))
        result = [mi, ma]
        while not pq.is_empty():
            elem, i, j = pq.pop()
            if ma - elem < result[1] - result[0]:
                result = [elem, ma]
            elif ma - elem == result[1] - result[0] and elem < result[0]:
                result = [elem, ma]
            l = mtx[i]
            if j + 1 < len(l):
                ma = max(ma, l[j + 1])
                pq.insert((l[j + 1], i, j + 1))
            else:
                break
        return result


print(
    Solution.get_smallest_range(
        [
            [1, 3, 5, 7, 9],
            [0, 2, 4, 6, 8],
            [2, 3, 5, 7, 11]
        ]
    )
)

print(
    Solution.get_smallest_range(
        [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12]
        ]
    )
)

print(Solution.get_smallest_range([[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]))
print(Solution.get_smallest_range([[1, 2, 3], [1, 2, 3], [1, 2, 3]]))

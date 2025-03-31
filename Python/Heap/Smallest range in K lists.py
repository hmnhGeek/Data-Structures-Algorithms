# Problem link - https://www.geeksforgeeks.org/problems/find-smallest-range-containing-elements-from-k-lists/1
# Solution - https://www.youtube.com/watch?v=0IqFMBatlhU


class MinHeap:
    def __init__(self):
        self.heap = []

    def is_empty(self):
        return len(self.heap) == 0

    def get_lci(self, pi):
        lci = 2 * pi + 1
        return lci if lci in range(len(self.heap)) else None

    def get_rci(self, pi):
        rci = 2 * pi + 2
        return rci if rci in range(len(self.heap)) else None

    def get_pi(self, ci):
        if ci == 0:
            return
        pi = int((ci - 1) / 2)
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
    def get_min_range(lists):
        """
            Time complexity is O(n*k*log(k)) and space complexity is O(k) for the min heap.
        """

        min_heap = MinHeap()

        # assume the range to be from -inf to inf
        result = [-1e6, 1e6]

        # take a max element with initial value as -inf.
        max_elem = -1e6

        # loop on the k lists and push their 0th elements into the min heap. This will take O(log(k)) time.
        for i in range(len(lists)):
            min_heap.insert((lists[i][0], i, 0))
            # while pushing, ensure that you get the maximum element out of the 0th elements of these k lists.
            # minimum will be given by min heap later.
            max_elem = max(max_elem, lists[i][0])

        # run an infinite loop. This loop will run for all the elements from all the lists in worst case, i.e.,
        # n*k times.
        while 1:
            # pop the minimum element. This will take O(log(k)) time.
            min_elem, i, j = min_heap.pop()

            # if the range max_elem - min_elem is less than current range (note that we did not include "="),
            # then update the current range to this new shorter range. If the difference had been equal, then
            # also we would keep the previous result only because as per the question, we need range with the smallest
            # min_elem. That is, if there are two valid ranges [1, 6] and [10, 16], the question prefers one with
            # the lower min_elem, i.e., [1, 6].
            if max_elem - min_elem < result[1] - result[0]:
                result = [min_elem, max_elem]

            # push the next element from the popped element list. This will take O(log(k)) time.
            if 0 <= j + 1 < len(lists[i]):
                min_heap.insert((lists[i][j + 1], i, j + 1))
                # ensure to update the max element by comparing the current max element with the new entered element.
                max_elem = max(max_elem, lists[i][j + 1])
            else:
                # if any of the lists get exhausted, break from the infinite loop. You now have the smallest range
                # including at least one element from each sorted lists.
                break

        # return the result range.
        return result


print(
    Solution.get_min_range(
        [
            [1, 3, 5, 7, 9],
            [0, 2, 4, 6, 8],
            [2, 3, 5, 7, 11]
        ]
    )
)

print(
    Solution.get_min_range(
        [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12]
        ]
    )
)

print(Solution.get_min_range([[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]))
print(Solution.get_min_range([[1, 2, 3], [1, 2, 3], [1, 2, 3]]))

print(
    Solution.get_min_range(
        [
            [2, 4, 5],
            [5, 6, 7]
        ]
    )
)

print(
    Solution.get_min_range(
        [
            [1, 1],
            [9, 12],
            [4, 9]
        ]
    )
)

print(
    Solution.get_min_range(
        [
            [4, 7, 30],
            [1, 2, 12],
            [20, 40, 50]
        ]
    )
)

print(
    Solution.get_min_range([[3, 6, 8, 12, 31]])
)

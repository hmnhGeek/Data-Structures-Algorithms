# Problem link - https://www.geeksforgeeks.org/problems/k-largest-elements4206/1


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
        if self.heap[min_child_index] > self.heap[rci]:
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
    def k_largest_elements(arr, k):
        """
            Overall time complexity is O(n * log(k)) and space complexity is O(2k).
        """

        # get the length of the array and initialize a Min Heap
        n = len(arr)
        min_heap = MinHeap()

        # push first k elements in to the min heap in k*log(k) time.
        for i in range(k):
            min_heap.insert(arr[i])

        # start iteration from kth index now. This will take O(n * log(k)) time.
        i = k
        while i < n:
            # if the ith element is greater than the top element of the heap, and since the heap is storing only k
            # elements, we've found an element which must be in the k largest elements. Thus remove the min element and
            # push the ith element, in 2*log(k) time.
            if arr[i] > min_heap.heap[0]:
                min_heap.pop()
                min_heap.insert(arr[i])
            i += 1

        # get the result in k*log(k) time.
        result = []
        while not min_heap.is_empty():
            result.append(min_heap.pop())
        return result


print(Solution.k_largest_elements([12, 5, 787, 1, 23], 2))
print(Solution.k_largest_elements([1, 23, 12, 9, 30, 2, 50], 3))
print(Solution.k_largest_elements([12, 23], 1))
print(Solution.k_largest_elements([11, 5, 12, 9, 44, 17, 2], 2))
print(Solution.k_largest_elements([3, 2, 1, 5, 6, 4], 2))
print(Solution.k_largest_elements([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
print(Solution.k_largest_elements([3, 4, 2, 1], 2))
print(Solution.k_largest_elements([2, 2, 3, 3, 1], 1))
print(Solution.k_largest_elements([0, 10, 1, 2, 2], 5))
print(Solution.k_largest_elements([-2, 12, -1, 1, 20, 1], 2))

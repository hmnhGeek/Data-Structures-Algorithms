# Problem link - https://www.geeksforgeeks.org/problems/minimize-max-distance-to-gas-station/1
# Solution - https://www.youtube.com/watch?v=kMSBvlZ-_HA&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=21


class Utility:
    @staticmethod
    def swap(arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]


class MaxHeap:
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

    def heapify_up(self, start_index):
        if start_index == 0:
            return
        pi = self.get_pi(start_index)
        lci, rci = self.get_lci(pi), self.get_rci(pi)
        max_child_index = self.get_max_child_index(lci, rci)
        if max_child_index is not None:
            if self.heap[pi] < self.heap[max_child_index]:
                Utility.swap(self.heap, pi, max_child_index)
            self.heapify_up(pi)

    def heapify_down(self, pi):
        lci, rci = self.get_lci(pi), self.get_rci(pi)
        max_child_index = self.get_max_child_index(lci, rci)
        if max_child_index is not None:
            if self.heap[pi] < self.heap[max_child_index]:
                Utility.swap(self.heap, pi, max_child_index)
            self.heapify_down(max_child_index)

    def insert(self, x):
        self.heap.append(x)
        self.heapify_up(len(self.heap) - 1)

    def pop(self):
        if self.is_empty():
            return
        item = self.heap[0]
        Utility.swap(self.heap, 0, -1)
        del self.heap[-1]
        self.heapify_down(0)
        return item


class Element:
    def __init__(self, distance, index, placed_count):
        self.d = distance
        self.i = index
        self.p = placed_count

    def __lt__(self, other):
        if self.d == other.d:
            return self.i < other.i
        return self.d < other.d

    def __gt__(self, other):
        if self.d == other.d:
            return self.i > other.i
        return self.d > other.d


class Solution:
    @staticmethod
    def place_gas_stations(arr, k):
        """
            Time complexity is O({n + k} * log(n)) and space complexity is O(n).
        """
        if k <= 0:
            return
        pq = MaxHeap()

        # takes O(n * log(n)) time
        Solution._initialize_pq(pq, arr)

        # takes O(k * log(n)) time
        while k > 0:
            element = pq.pop()
            distance, index, placed_count = element.d, element.i, element.p
            new_distance = distance * (placed_count + 1) / (placed_count + 2)
            pq.insert(Element(new_distance, index, placed_count + 1))
            k -= 1
        return pq.pop().d

    @staticmethod
    def _initialize_pq(pq, arr):
        for i in range(len(arr) - 1):
            element = Element(arr[i + 1] - arr[i], i, 0)
            pq.insert(element)


print(Solution.place_gas_stations([1, 2, 3, 4, 5, 6, 7], 6))
print(Solution.place_gas_stations([1, 2, 3, 4, 5], 4))
print(Solution.place_gas_stations(list(range(1, 11)), 1))
print(Solution.place_gas_stations([3, 6, 12, 19, 33, 44, 67, 72, 89, 95], 2))
print(Solution.place_gas_stations([1, 13, 17, 23], 5))

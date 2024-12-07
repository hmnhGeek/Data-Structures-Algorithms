# Problem link - https://www.naukri.com/code360/problems/minimise-max-distance_7541449
# Solution - https://www.youtube.com/watch?v=kMSBvlZ-_HA&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=21


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
    def place_gas_stations(arr, k):
        """
            Overall time complexity is O({n + k} * log(n)) time and O(n) space.
        """

        n = len(arr)

        # define an array of length (n - 1) storing the number of gas stations placed in each slot. We can place the gas
        # stations outside the array as well but that won't minimize the distance between the gas stations and so, we
        # must place them within the slots.
        slots = [0] * (n - 1)

        # define a max heap
        max_heap = MaxHeap()

        # push the (slot_length, slot_index) into max heap. The idea is to pop from the max heap continuously to always
        # get the max length slot so that we can place a new gas station in that slot. This will take O(n*log(n)) time.
        # And the space used will be O(n).
        for i in range(n - 1):
            diff = arr[i + 1] - arr[i]
            slot_length = (diff / (slots[i] + 1))
            max_heap.insert((slot_length, i))

        # now start placing the `k` gas stations. This is the minimization step. It will take O(k * log(n)) time.
        for i in range(k):
            # pop the max length slot in O(log(n)) time.
            diff, idx = max_heap.pop()
            # increment the gas stations placed at this index.
            slots[idx] += 1
            # update the max diff in this slot as we are evenly dividing the slot by the number of gas stations.
            new_length = (diff / (slots[idx] + 1))
            # insert it back into the max heap.
            max_heap.insert((new_length, idx))

        # at the end, the max diff will always be on the top of the heap, return it.
        max_diff_between_stations, _ = max_heap.pop()
        return max_diff_between_stations


print(Solution.place_gas_stations([1, 2, 3, 4, 5], 4))
print(Solution.place_gas_stations([1, 2, 3, 4, 5, 6, 7], 6))
print(Solution.place_gas_stations([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1))
print(Solution.place_gas_stations([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 9))
print(Solution.place_gas_stations([3, 6, 12, 19, 33, 44, 67, 72, 89, 95], 2))

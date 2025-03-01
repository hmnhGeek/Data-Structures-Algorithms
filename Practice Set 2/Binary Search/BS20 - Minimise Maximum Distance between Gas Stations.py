# Problem link - https://www.geeksforgeeks.org/problems/minimize-max-distance-to-gas-station/1
# Solution - https://www.youtube.com/watch?v=kMSBvlZ-_HA&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=21


class LinearSolution:
    @staticmethod
    def minimize_the_max_distance(arr, k):
        """
            Time complexity is O(nk) and space complexity is O(n).
        """

        # edge case
        if k <= 0:
            return -1

        # store the length of the array in `n` for easier access.
        n = len(arr)

        # create a (n - 1) length list of 0s storing the count of gas stations placed inside the ith slot. This should
        # take O(n) space.
        how_many = [0] * (n - 1)

        # now start placing the k gas stations in O(n * k) time.
        for gas_station in range(k):
            # for each iteration, let us try to find the slot with maximum difference as that is the one which we want
            # to minimize.
            max_slot = -1e6
            max_slot_index = -1

            # now loop on the slots in O(n) time.
            for i in range(n - 1):
                # get the slot difference
                slot_difference = arr[i + 1] - arr[i]
                # check what would be the new slot difference if we place a gas station inside this slot.
                new_slot_difference = slot_difference/(how_many[i] + 1)
                # new_slot_difference is directly proportional to slot_difference and so we can use it to updat the max
                # slot.
                if max_slot < new_slot_difference:
                    max_slot = new_slot_difference
                    max_slot_index = i

            # once the max_slot_index is found, add a gas station in that slot.
            how_many[max_slot_index] += 1

        ############ FINDING THE MAXIMUM DISTANCE IN THE UPDATED ARRAY AFTER GAS STATIONS PLACEMENTS ################

        # let's assume that the max distance between any two gas stations is -inf.
        minimum_max_distance = -1e6

        # loop on the slots in O(n) time.
        for i in range(n - 1):
            # get the evenly distributed gas stations distance at this slot.
            slot_difference = (arr[i + 1] - arr[i])/(how_many[i] + 1)
            # and take the maximum distance.
            minimum_max_distance = max(minimum_max_distance, slot_difference)

        # finally return the max distance.
        return minimum_max_distance


print("Linear Search Solution")
print(LinearSolution.minimize_the_max_distance([1,2,3,4,5,6,7], 6))
print(LinearSolution.minimize_the_max_distance([1, 2, 3, 4, 5], 4))
print(LinearSolution.minimize_the_max_distance(list(range(1, 11)), 1))
print(LinearSolution.minimize_the_max_distance([3, 6, 12, 19, 33, 44, 67, 72, 89, 95], 2))
print(LinearSolution.minimize_the_max_distance([1, 13, 17, 23], 5))
print()


class Slot:
    def __init__(self, length, index):
        self.length = length
        self.index = index


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

    def get_max_child_index(self, lci, rci):
        if lci is None and rci is None:
            return
        if lci is None:
            return rci
        if rci is None:
            return lci
        max_child_index = lci
        if self.heap[rci].length > self.heap[max_child_index].length:
            max_child_index = rci
        return max_child_index

    def max_heapify_up(self, start_index):
        if start_index == 0:
            return
        pi = self.get_pi(start_index)
        lci, rci = self.get_lci(pi), self.get_rci(pi)
        max_child_index = self.get_max_child_index(lci, rci)
        if max_child_index is not None:
            if self.heap[pi].length < self.heap[max_child_index].length:
                self.heap[pi], self.heap[max_child_index] = self.heap[max_child_index], self.heap[pi]
            self.max_heapify_up(pi)

    def max_heapify_down(self, pi):
        lci, rci = self.get_lci(pi), self.get_rci(pi)
        max_child_index = self.get_max_child_index(lci, rci)
        if max_child_index is not None:
            if self.heap[pi].length < self.heap[max_child_index].length:
                self.heap[pi], self.heap[max_child_index] = self.heap[max_child_index], self.heap[pi]
            self.max_heapify_down(max_child_index)

    def insert(self, x: Slot):
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
    def _push_initial_state(pq: MinHeap, arr, n):
        """
            Time complexity is O(n * log(n)) and space complexity is O(n).
        """
        for i in range(n - 1):
            pq.insert(Slot(arr[i + 1] - arr[i], i))

    @staticmethod
    def minimize_the_max_distance(arr, k):
        """
            Time complexity is O({n + k} * log(n)) time and O(n) space.
        """

        # edge case.
        if k <= 0:
            return -1

        # store the length of array for ease of access.
        n = len(arr)

        # define a slots array denoting the number of gas stations placed in each slot. This will take O(n) space.
        gas_stations_in_slots = [0] * (n - 1)

        # define a max heap and push the slots into it in O(n * log(n)) time and O(n) space.
        pq = MinHeap()
        Solution._push_initial_state(pq, arr, n)

        # loop on the gas stations in k iterations.
        for i in range(k):
            # pop the max length slot in O(log(n)) time.
            slot = pq.pop()

            # get the length and index of the max slot.
            max_slot, max_slot_index = slot.length, slot.index

            # place the gas station at this slot.
            gas_stations_in_slots[max_slot_index] += 1

            # get the original length of the slot
            original_length = max_slot * gas_stations_in_slots[max_slot_index]

            # get the new length of the slot.
            new_length = original_length/(gas_stations_in_slots[max_slot_index] + 1)

            # insert back into the max heap in O(log(n)) time.
            pq.insert(Slot(new_length, max_slot_index))

        # return the max distance in O(1) time.
        return pq.heap[0].length


print("Max Heap Solution")
print(Solution.minimize_the_max_distance([1,2,3,4,5,6,7], 6))
print(Solution.minimize_the_max_distance([1, 2, 3, 4, 5], 4))
print(Solution.minimize_the_max_distance(list(range(1, 11)), 1))
print(Solution.minimize_the_max_distance([3, 6, 12, 19, 33, 44, 67, 72, 89, 95], 2))
print(Solution.minimize_the_max_distance([1, 13, 17, 23], 5))
print()
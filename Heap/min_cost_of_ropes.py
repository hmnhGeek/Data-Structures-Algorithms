# Problem link - https://www.geeksforgeeks.org/problems/minimum-cost-of-ropes-1587115620/1


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
            return None
        if lci is None:
            return rci
        if rci is None:
            return lci
        min_child_index = lci
        if self.heap[rci] < self.heap[min_child_index]:
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


def get_min_cost_of_connecting_ropes(ropes):
    """
        Overall time complexity is O(n*log(n)) and space complexity is O(n) for the min heap.
    """

    # if there are no ropes, return 0 cost
    if len(ropes) == 0:
        return 0

    # if there is only one rope, return the cost as the rope length
    if len(ropes) == 1:
        return ropes[0]

    # initialize a min heap to solve this problem and put all the ropes into this min heap. This shall take O(n*log(n))
    # time and O(n) space.
    min_heap = MinHeap()
    for rope in ropes:
        min_heap.insert(rope)

    # initialize a cost variable to keep track of the cost.
    cost = 0

    # while the heap is not empty, run this algorithm. This will run for n ropes. Overall O(n*log(n)) time.
    while not min_heap.is_empty():
        # pop two min-length ropes, in O(log(n)) time
        rope1, rope2 = min_heap.pop(), min_heap.pop()

        # add the sum of their lengths to the cost
        cost += (rope1 + rope2)

        # if the min heap is not yet empty, i.e., we have more ropes to connect, then add this newly formed rope back
        # to the min heap, so that in next iteration, other ropes can be connected with this rope as well. This will
        # take O(log(n)) time.
        if not min_heap.is_empty():
            min_heap.insert(rope1 + rope2)

    # finally return the cost
    return cost


print(get_min_cost_of_connecting_ropes([4, 3, 2, 6]))
print(get_min_cost_of_connecting_ropes([4, 2, 7, 6, 9]))
print(get_min_cost_of_connecting_ropes([1, 2, 3]))
print(get_min_cost_of_connecting_ropes([1, 2, 3, 4, 5]))
print(get_min_cost_of_connecting_ropes([10]))
print(get_min_cost_of_connecting_ropes([]))

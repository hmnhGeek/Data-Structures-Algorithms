# Problem link - https://www.geeksforgeeks.org/problems/find-median-in-a-stream-1587115620/1


class MinHeap:
    def __init__(self):
        self.heap = []

    def size(self):
        return len(self.heap)

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

    def top(self):
        if self.is_empty():
            return -1e6
        return self.heap[0]


class MaxHeap:
    def __init__(self):
        self.heap = []

    def size(self):
        return len(self.heap)

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

    def top(self):
        if self.is_empty():
            return 1e6
        return self.heap[0]


class Stream:
    def __init__(self):
        self.min_heap = MinHeap()
        self.max_heap = MaxHeap()
        self.size = 0

    def _manage_tops(self):
        # as explained in the parent call, the max on the left half should be smaller or equal to the min on the right
        # half. If that is not the case, then exchange the tops of the heaps.
        if self.max_heap.top() > self.min_heap.top():
            temp1 = self.max_heap.pop()
            temp2 = self.min_heap.pop()
            if temp2:
                self.max_heap.insert(temp2)
            if temp1:
                self.min_heap.insert(temp1)

    def _manage_heap_sizes(self):
        # as explained in the parent call, we will keep the left heap light. If the size of left heap (max heap) has
        # become heavier than the right heap (because we are just inserting in the max heap), then pop from left heap
        # and push it to right heap. This way, we are ensuring that the weights of both the heaps are either same or
        # the right heap is heavier than the left heap.
        if self.max_heap.size() > self.min_heap.size():
            self.min_heap.insert(self.max_heap.pop())

    def add(self, x):
        """
            The time complexity of adding to stream is thus O(n*log(n)) and space complexity is O(n) for maintaining the
            heaps.
        """

        # we will always insert in max heap (left heap) in O(n*log(n)) time.
        self.max_heap.insert(x)
        # increment the size of the stream.
        self.size += 1
        # now, call this method to check if the tops of both the heaps are in correct order or not. The top of left
        # heap that is max heap, should be less than or equal to the top of min heap (right heap). Why? Because the
        # median always lies in the middle. The max of left half (given by the max heap) should be less than or equal
        # to the min of right half (given by the min heap). This should take O(n*log(n)) time whenever needed,
        # otherwise its O(1) time operation.
        self._manage_tops()
        # we will always keep the left heap (max heap) light-weight or equal in weight with the right heap (min heap).
        # This will also take O(n*log(n)) time if required, else it will also be O(1) operation.
        self._manage_heap_sizes()

    def get_median(self):
        """
            Time complexity is O(1) and space complexity is O(1).
        """

        # if the size of the stream is even, then the median is the average of the tops of both the heaps. Don't we
        # need to place checks on `.top` if it is None or not? No, because if the stream size has become even, then
        # both heaps will contain at least one element.
        if self.size % 2 == 0:
            return (self.max_heap.top() + self.min_heap.top()) / 2
        # else if the stream size is odd, then we know that median will always lie on the min heap because we have
        # ensured that the right heap is slightly heavier than the left heap in odd case.
        else:
            return self.min_heap.top()


def test_stream(*args):
    stream = Stream()
    for i in args:
        stream.add(i)
        print(stream.get_median(), end=", ")
    print()


test_stream(5, 15, 1, 3)
test_stream(2, 6, 8, 0, 9, 9, 7)
test_stream(2, 7, 4, 3, 6, 8, 9, 6, 9, 4, 3, 0)
test_stream(8, 4, 7, 3, 6, 8)
test_stream(1, 3, 2)

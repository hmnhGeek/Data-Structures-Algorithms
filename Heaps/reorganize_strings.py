# Problem link - https://leetcode.com/problems/reorganize-string/


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
        max_child_index = lci
        if self.heap[rci][1] > self.heap[max_child_index][1]:
            max_child_index = rci
        return max_child_index

    def max_heapify_up(self, start_index):
        if start_index == 0:
            return
        pi = self.get_pi(start_index)
        lci, rci = self.get_lci(pi), self.get_rci(pi)
        max_child_index = self.get_max_child_index(lci, rci)

        if max_child_index is not None:
            if self.heap[pi][1] < self.heap[max_child_index][1]:
                self.heap[pi], self.heap[max_child_index] = self.heap[max_child_index], self.heap[pi]
            self.max_heapify_up(pi)

    def max_heapify_down(self, pi):
        lci, rci = self.get_lci(pi), self.get_rci(pi)
        max_child_index = self.get_max_child_index(lci, rci)

        if max_child_index is not None:
            if self.heap[pi][1] < self.heap[max_child_index][1]:
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


def reorganize_string(string: str) -> str:
    """
        Time complexity is O(n*log(m)) and space complexity is O(m).
    """

    # initialize a max heap to get the most frequent character in O(log(m)) time where `m` is the number of
    # distinct characters in the string.
    max_heap = MaxHeap()

    # store a `prev` keyword which will be used to track the last character used in the resultant string.
    prev = None

    # push the frequencies of each character into the max heap. This will take O(n + m*log(m)) time
    frequencies = dict(Counter(string))
    # This will take O(m*log(m)) time and O(m) space.
    for k, v in frequencies.items():
        max_heap.insert((k, v))

    # store a resultant string
    result = ""

    # while the heap is not empty, this will run for `n` times. Thus, it would take O(n*log(m)) time.
    while not max_heap.is_empty():
        # pop the most frequent in O(log(m)) time.
        character, frequency = max_heap.pop()
        result += character

        # if there was any prev character used in the resultant string, push it back to max heap
        # because it can be used again now. Also, push only if the frequency is more than 0. This
        # would take O(log(m)) time.
        if prev is not None:
            if prev[1] > 0:
                max_heap.insert(prev)

        # update the `prev` to current character with a decremented frequency.
        prev = (character, frequency - 1)

    # finally after the heap is empty, check if there is still some character left in prev with > 0 frequency.
    # This would mean that there will be adjacent-same characters, hence the reorganization is not possible.
    # We should thus return a blank string.
    if prev is not None and prev[1] > 0:
        return ""

    # return result.
    return result


print(reorganize_string("aab"))
print(reorganize_string("aaab"))
print(reorganize_string("geeksforgeeks"))
print(reorganize_string("bbbb"))
print(reorganize_string("aaabc"))
print(reorganize_string("aaabb"))
print(reorganize_string("aaaabc"))
# Problem link - https://www.geeksforgeeks.org/problems/find-smallest-range-containing-elements-from-k-lists/1

class MinHeap:
    def __init__(self):
        self.heap = []

    def get_lci(self, pi):
        lci = 2*pi + 1
        return lci if lci in range(len(self.heap)) else None

    def get_rci(self, pi):
        rci = 2*pi + 2
        return rci if rci in range(len(self.heap)) else None

    def get_pi(self, ci):
        pi = int((ci - 1)/2)
        return pi if pi in range(len(self.heap)) else None

    def insert(self, x, i, j):
        self.heap.append([x, i, j])
        self.min_heapify_up(len(self.heap) - 1)

    def is_empty(self):
        return len(self.heap) == 0

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

    def get_min_child_index(self, lci, rci):
        if lci is None and rci is None:
            return None
        if lci is None:
            return rci
        if rci is None:
            return lci

        min_child_index = lci
        if self.heap[min_child_index][0] > self.heap[rci][0]:
            min_child_index = rci

        return min_child_index

    def pop(self):
        if len(self.heap) == 0:
            return
        last_index = len(self.heap) - 1
        self.heap[last_index], self.heap[0] = self.heap[0], self.heap[last_index]
        item = self.heap[last_index]
        del self.heap[last_index]
        self.min_heapify_down(0)
        return item

    def min_heapify_down(self, pi):
        lci, rci = self.get_lci(pi), self.get_rci(pi)
        min_child_index = self.get_min_child_index(lci, rci)

        if min_child_index is not None:
            if self.heap[pi][0] > self.heap[min_child_index][0]:
                self.heap[pi], self.heap[min_child_index] = self.heap[min_child_index], self.heap[pi]
            self.min_heapify_down(min_child_index)


def get_min_range(mtx):
    '''
        The entire algorithm can be explained this way.

        1. Initialize a global range from (-inf, inf).
        2. Initialize a local range from (inf, -inf).
        3. Push the 0th elements from the k rows into
           a min heap. While pushing into min heap,
           update maxi value continuously. This will
           ensure that maxi has max value of the 0th
           column.
        4. If the heap is not empty, continue to 5,
           else return the global range.
        5. Change the mini value to the popped element
           from the heap. Also extract the list index
           and the element index from this list as i, j.
        6. Check if maxi - mini < global range. If yes,
           go to 7, else go to 8.
        7. Update the global minimum to mini and global
           maximum to maxi.
        8. In the ith list (obtained in 5), check if
           j + 1 is a valid index. If not, break and
           return the global range, else continue to
           step 9.
        9. Push the next element at index j + 1 in ith
           row to the heap. At the same time, update
           the maxi value with max(maxi, next element).
        10. Go to step 4.

        Overall time complexity is O(nk log(k)) and
        Overall space complexity is O(k) for the min heap.

        Use this video to better understand the logic.
        Video - https://www.youtube.com/watch?v=Fqal25ZgEDo
    '''

    k = len(mtx)
    n = len(mtx[0])
    heap = MinHeap()

    # define constants for infinities.
    INT_MAX, INT_MIN = float('inf'), float('-inf')

    # store answer as (-inf, inf), i.e., longest possible range on the number line.
    answer = [INT_MIN, INT_MAX]

    # initialize mini and maxi with opposite polarity of infinities.
    mini, maxi = INT_MAX, INT_MIN

    # insert the first column into the heap.
    # also just update maxi value from the 0th column,
    # please don't update mini value. This step will
    # take O(k*log(k)) time (due to min heapify post insertion).
    for i in range(k):
        heap.insert(mtx[i][0], i, 0)
        maxi = max(maxi, mtx[i][0])

    # till the time heap does not get empty, run this block.
    # it is ensured that n*k elements will go into the heap
    # (in the worst case, otherwise less  > n and < n*k),
    # until you are at the last element of one of the lists.
    # So this will take O(n*k*log(k)) time.
    while not heap.is_empty():
        # extract the minimum value out of the heap.
        # No need to do mini = min(mini, heap.pop()[0]),
        # simply update mini = heap.pop()[0] because we
        # want to check that for this minimum value in
        # the heap, can we reduce the range further. At
        # each step we are trying to move to the right on
        # the number line by increasing the mini value.
        # This will take O(log(k)) time to min heapify
        # post popping the element.
        mini, i, j = heap.pop()

        # maxi was already non-infinite. Check if maxi - mini
        # is less than global range value. If yes, update the
        # global range with correct values.
        if maxi - mini < answer[1] - answer[0]:
            answer = [mini, maxi]

        # now, check if j + 1 is not out of bounds. If it is not,
        # then simply push the next element from the row of mini
        # (the one that we just updated with) into the heap. Also,
        # as you push into the heap, ensure that you update the
        # maxi value for the next iteration. At this point, we
        # would say that maxi = max(maxi, next_element). However,
        # if j + 1 is out of bounds, we have nothing else to push
        # into the heap; break from the loop and return the global
        # range. This will again take O(log(k)) time.
        if j + 1 in range(n):
            heap.insert(mtx[i][j + 1], i, j + 1)
            maxi = max(maxi, mtx[i][j + 1])
        else:
            break

    return answer

print(
    get_min_range(
        [
            [4, 10, 15, 24],
            [0, 9, 12, 20],
            [5, 18, 22, 30]
        ]
    )
)

print(
    get_min_range(
        [[1, 3, 5, 7, 9],
         [0, 2, 4, 6, 8],
         [2, 3, 5, 7, 11]]
    )
)

print(
    get_min_range(
        [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12]
        ]
    )
)
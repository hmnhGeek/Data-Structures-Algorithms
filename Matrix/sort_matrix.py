# Problem link - https://www.geeksforgeeks.org/problems/sorted-matrix2333/1


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


def heap_sort(arr):
    # Overall time complexity is O(nlog(n)) and space complexity is O(n).
    min_heap = MinHeap()

    # push all the elements of the array into the heap. This will take O(n*log(n)) time and O(n) space.
    for i in arr:
        min_heap.insert(i)

    # build back the sorted array in O(n*log(n)) time.
    counter = 0
    while not min_heap.is_empty():
        arr[counter] = min_heap.pop()
        counter += 1


def sort_matrix(mtx):
    # Overall time complexity is O(mn*log(mn)) and space complexity is O(mn).

    # store the dimensions of the matrix
    n, m = len(mtx), len(mtx[0])

    # these indices will be useful in building up the sorted matrix.
    i_counter, j_counter = 0, 0

    # construct a copy matrix of size n*m with None values. This will take O(m*n) space.
    sorted_mtx = [[None for _ in range(m)] for _ in range(n)]

    # flatten the matrix in an array.
    flattened_mtx = []
    for i in range(n):
        for j in range(m):
            flattened_mtx.append(mtx[i][j])

    # sort the flattened matrix in O(nm * log(nm)) time and O(nm) space.
    heap_sort(flattened_mtx)

    # build back the sorted matrix by traversing into the sorted flattened matrix. This will take O(m*n) time.
    for i in flattened_mtx:
        sorted_mtx[i_counter][j_counter] = i
        # increment the column each time you assign an element
        j_counter += 1
        # if at any point the j_counter exceeds the right boundary, move to the next row.
        if j_counter == m:
            j_counter = 0
            i_counter += 1

    # return the sorted matrix.
    return sorted_mtx


mtx1 = [[10, 20, 30, 40],
        [15, 25, 35, 45],
        [27, 29, 37, 48],
        [32, 33, 39, 50]]
sorted_mtx1 = sort_matrix(mtx1)
for i in sorted_mtx1:
    print(i)

mtx2 = [[1, 5, 3], [2, 8, 7], [4, 6, 9]]
sorted_mtx2 = sort_matrix(mtx2)
for i in sorted_mtx2:
    print(i)
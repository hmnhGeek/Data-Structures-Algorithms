# Problem link - https://www.geeksforgeeks.org/dsa/sort-k-sorted-doubly-linked-list/
# Solution - https://www.youtube.com/watch?v=9jdqdhsynmA


class MinHeap:
    def __init__(self):
        self.heap = []

    def is_empty(self):
        return len(self.heap) == 0

    def get_lci(self, pi):
        ci = 2 * pi + 1
        return ci if ci in range(len(self.heap)) else None

    def get_rci(self, pi):
        ci = 2 * pi + 2
        return ci if ci in range(len(self.heap)) else None

    def get_pi(self, ci):
        if ci == 0:
            return
        pi = int((ci - 1)/2)
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
        lci = self.get_lci(pi)
        rci = self.get_rci(pi)
        min_child_index = self.get_min_child_index(lci, rci)
        if min_child_index is not None:
            if self.heap[pi] > self.heap[min_child_index]:
                self.heap[pi], self.heap[min_child_index] = self.heap[min_child_index], self.heap[pi]
            self.min_heapify_up(pi)

    def min_heapify_down(self, pi):
        lci = self.get_lci(pi)
        rci = self.get_rci(pi)
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


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = self.next = None

    def __lt__(self, other):
        return self.data < other.data

    def __gt__(self, other):
        return self.data > other.data


class DoublyLinkedList:
    def __init__(self):
        self.head = self.tail = None
        self.length = 0

    def is_empty(self):
        return self.length == 0

    def push(self, x):
        node = Node(x)
        if self.is_empty():
            self.head = self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.length += 1

    def build(self, *args):
        for i in args:
            self.push(i)

    def __str__(self):
        if self.is_empty():
            return "[]"
        result = "["
        curr = self.head
        while curr != self.tail:
            result += f"{curr.data}, "
            curr = curr.next
        result += f"{self.tail.data}]"
        return result


class Solution:
    @staticmethod
    def sort_dll(dll: DoublyLinkedList, k: int):
        """
            Time complexity is O(n * log(k)) and space complexity is O(k).
        """

        pq = MinHeap()
        curr = dll.head
        counter = 0

        # store k + 1 elements and not k because each node is k units from its sorted position.
        while counter != k + 1:
            pq.insert(curr)
            curr = curr.next
            counter += 1

        dummy = Node(None)
        temp = dummy

        # This will take O(n * log(k)) time.
        while not pq.is_empty():
            node = pq.pop()
            temp.next = node
            node.prev = temp
            temp = temp.next
            if curr is not None:
                pq.insert(curr)
                curr = curr.next
        dll.head = dummy.next
        dll.tail = temp

    @staticmethod
    def test(*args):
        k = args[-1]
        dll = DoublyLinkedList()
        dll.build(*args[:-1])
        print("Before: ", dll)
        Solution.sort_dll(dll, k)
        print("After: ", dll)
        print()


Solution.test(3, 2, 1, 5, 6, 4, 2)


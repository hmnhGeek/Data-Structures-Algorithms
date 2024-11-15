from typing import List


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = self.tail = None

    def push(self, x):
        node = Node(x)
        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def _build(self, _list):
        for i in _list:
            self.push(i)

    def show(self):
        curr = self.head
        while curr is not None:
            print(curr.data, end=" --> ")
            curr = curr.next
        print()


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
        if self.heap[rci].data < self.heap[min_child_index].data:
            min_child_index = rci
        return min_child_index

    def min_heapify_up(self, start_index):
        if start_index == 0:
            return
        pi = self.get_pi(start_index)
        lci, rci = self.get_lci(pi), self.get_rci(pi)
        min_child_index = self.get_min_child_index(lci, rci)
        if min_child_index is not None:
            if self.heap[pi].data > self.heap[min_child_index].data:
                self.heap[pi], self.heap[min_child_index] = self.heap[min_child_index], self.heap[pi]
            self.min_heapify_up(pi)

    def min_heapify_down(self, pi):
        lci, rci = self.get_lci(pi), self.get_rci(pi)
        min_child_index = self.get_min_child_index(lci, rci)
        if min_child_index is not None:
            if self.heap[pi].data > self.heap[min_child_index].data:
                self.heap[pi], self.heap[min_child_index] = self.heap[min_child_index], self.heap[pi]
            self.min_heapify_down(min_child_index)

    def insert(self, x: Node):
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
    def merge_sorted_linked_lists(linked_lists: List[LinkedList]) -> LinkedList:
        min_heap = MinHeap()
        dummy_node = starter = Node(-1)
        for linked_list in linked_lists:
            min_heap.insert(linked_list.head)

        while not min_heap.is_empty():
            node = min_heap.pop()
            starter.next = node
            if node.next is not None:
                min_heap.insert(node.next)
            node.next = None
            starter = node

        result = LinkedList()
        result.head = dummy_node.next
        result.tail = starter
        return result


def test(lists: List[List[int]]):
    input_linked_lists = []
    for l in lists:
        ll = LinkedList()
        ll._build(l)
        input_linked_lists.append(ll)
    print("Input linked lists")
    for ll in input_linked_lists:
        ll.show()
    print()
    merged_linked_list = Solution.merge_sorted_linked_lists(input_linked_lists)
    print("Merged linked list")
    merged_linked_list.show()
    print()
    print("-----------------------------")


test(
    [
        [1, 2, 3],
        [4, 5],
        [5, 6],
        [7, 8]
    ]
)

test(
    [
        [1, 3],
        [4, 5, 6],
        [8]
    ]
)

test([[1, 4, 5], [1, 3, 4], [2, 6]])

from typing import List


class MinHeap:
    def __init__(self):
        self.heap = []

    def is_empty(self):
        return len(self.heap) == 0

    def get_lci(self, pi):
        ci = 2*pi + 1
        if 0 <= ci < len(self.heap):
            return ci
        return None

    def get_rci(self, pi):
        ci = 2 * pi + 2
        if 0 <= ci < len(self.heap):
            return ci
        return None

    def get_pi(self, ci):
        if ci == 0:
            return
        pi = int((ci - 1)/2)
        if 0 <= pi < len(self.heap):
            return pi
        return None

    def get_min_child_index(self, lci, rci):
        if lci is None and rci is None:
            return
        if lci is None:
            return rci
        if rci is None:
            return lci
        mci = lci
        if self.heap[rci] < self.heap[mci]:
            mci = rci
        return mci

    def heapify_up(self, start_index):
        if start_index == 0:
            return
        pi = self.get_pi(start_index)
        lci, rci = self.get_lci(pi), self.get_rci(pi)
        min_child_index = self.get_min_child_index(lci, rci)
        if min_child_index is not None:
            if self.heap[pi] > self.heap[min_child_index]:
                self.heap[pi], self.heap[min_child_index] = self.heap[min_child_index], self.heap[pi]
            self.heapify_up(pi)

    def heapify_down(self, pi):
        lci, rci = self.get_lci(pi), self.get_rci(pi)
        min_child_index = self.get_min_child_index(lci, rci)
        if min_child_index is not None:
            if self.heap[pi] > self.heap[min_child_index]:
                self.heap[pi], self.heap[min_child_index] = self.heap[min_child_index], self.heap[pi]
            self.heapify_down(min_child_index)

    def insert(self, x):
        self.heap.append(x)
        self.heapify_up(len(self.heap) - 1)

    def pop(self):
        if self.is_empty():
            return
        item = self.heap[0]
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        del self.heap[-1]
        self.heapify_down(0)
        return item


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __lt__(self, other):
        return self.data < other.data

    def __gt__(self, other):
        return self.data > other.data


class LinkedList:
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
    def merge_k_sorted_linked_lists(linked_lists: List[LinkedList]) -> LinkedList:
        min_heap = MinHeap()
        merged_linked_list = LinkedList()
        for linked_list in linked_lists:
            min_heap.insert(linked_list.head)
        dummy_node = temp = Node(None)
        merged_linked_list_length = 0
        while not min_heap.is_empty():
            node = min_heap.pop()
            merged_linked_list_length += 1
            temp.next = node
            if node.next is not None:
                min_heap.insert(node.next)
            node.next = None
            temp = node
        merged_linked_list.head = dummy_node.next
        merged_linked_list.tail = temp
        merged_linked_list.length = merged_linked_list_length
        return merged_linked_list


# Example 1
l1 = LinkedList()
l1.build(1, 2, 3)
l2 = LinkedList()
l2.build(4, 5)
l3 = LinkedList()
l3.build(5, 6)
l4 = LinkedList()
l4.build(7, 8)
merged = Solution.merge_k_sorted_linked_lists([l1, l2, l3, l4])
print(merged)

# Example 2
l1 = LinkedList()
l1.build(1, 3)
l2 = LinkedList()
l2.build(4, 5, 6)
l3 = LinkedList()
l3.build(8)
merged = Solution.merge_k_sorted_linked_lists([l1, l2, l3])
print(merged)

# Example 3
l1 = LinkedList()
l1.build(1, 3, 7)
l2 = LinkedList()
l2.build(2, 4, 8)
l3 = LinkedList()
l3.build(9)
merged = Solution.merge_k_sorted_linked_lists([l1, l2, l3])
print(merged)

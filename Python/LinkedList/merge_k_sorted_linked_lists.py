# Problem link - https://www.geeksforgeeks.org/problems/merge-k-sorted-linked-lists/1


from typing import List


class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = self.tail = None

    def insert(self, x: int):
        node = Node(x)

        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def build(self, arr: List[int]):
        for element in arr:
            self.insert(element)

    def show(self):
        curr = self.head
        while curr is not None:
            print(curr.data, end=" ")
            curr = curr.next
        print()


class MinHeap:
    """
        This min heap will store data of type Node.
    """
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


class SortedLinkedListMerger:
    def __init__(self, linked_lists: List[LinkedList]):
        self.lls = linked_lists
        self.min_heap = MinHeap()
        self.merged_list = LinkedList()

    def merge(self):
        # Overall time complexity is O(n*k*log(k)) and O(n + k) space.

        # create a dummy node, this will be useful for finding the starting point of the merged list
        dummy_node = Node(-1)
        curr = dummy_node

        # first push the k linked lists heads into the min heap in O(log(k)) time with O(k) space for the heap.
        for linked_list in self.lls:
            self.min_heap.insert(linked_list.head)

        # This will run for all the nodes in the heap, i.e., n*k times
        while not self.min_heap.is_empty():
            # O(log(k)) operation
            node = self.min_heap.pop()

            # again an O(log(k)) operation; we want to push the next node of the popped node to maintain sorted order.
            if node.next is not None:
                self.min_heap.insert(node.next)

            # in the merged section, point curr's next to the popped node
            curr.next = node

            # then update the curr to popped node.
            curr = node

        # head of the merged list is dummy node's next
        self.merged_list.head = dummy_node.next

        # tail of the merged list is the last node in the traversal, i.e., curr.
        self.merged_list.tail = curr


print("Example 1")
l1 = LinkedList()
l1.build([1, 2, 3])
l2 = LinkedList()
l2.build([4, 5])
l3 = LinkedList()
l3.build([5, 6])
l4 = LinkedList()
l4.build([7, 8])
linked_lists = [l1, l2, l3, l4]
sorted_linked_list_merger = SortedLinkedListMerger(linked_lists)
sorted_linked_list_merger.merge()
sorted_linked_list_merger.merged_list.show()

print("\nExample 2")
l1 = LinkedList()
l1.build([1, 3])
l2 = LinkedList()
l2.build([4, 5, 6])
l3 = LinkedList()
l3.build([8])
linked_lists = [l1, l2, l3]
sorted_linked_list_merger = SortedLinkedListMerger(linked_lists)
sorted_linked_list_merger.merge()
sorted_linked_list_merger.merged_list.show()
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
        self.next = None


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

    def show(self):
        curr = self.head
        while curr is not None:
            print(curr.data, end=" ")
            curr = curr.next
        print()

    def build(self, *args):
        for i in args:
            self.push(i)


class Solution:
    @staticmethod
    def merge(linked_lists):
        """
            Time complexity is O(n * log(k)) and space complexity is O(k).
        """

        # initialize a min heap and a dummy node variable to get the head of the merged list.
        min_heap = MinHeap()
        dummy_node = temp = Node(None)

        # loop in the k lists and push their heads into the min heap in O(k * log(k)) time.
        k = len(linked_lists)
        for i in range(k):
            min_heap.insert(linked_lists[i].head)

        # while the min heap is not empty. This will run for n times (all the nodes).
        while not min_heap.is_empty():
            # get the smallest node in O(log(k)) time.
            node = min_heap.pop()

            # store the next node reference.
            next_node = node.next

            # add the node to merged list
            temp.next = node
            temp = node

            # if next node is present, add it to min heap in O(log(k)) time.
            if next_node is not None:
                min_heap.insert(next_node)

        # finally, create a new merged linked list with head as dummy.next and tail as temp.
        merged_list = LinkedList()
        merged_list.head = dummy_node.next
        merged_list.tail = temp
        return merged_list


# Example 1
l1 = LinkedList()
l1.build(1, 2, 3)
l2 = LinkedList()
l2.build(4, 5)
l3 = LinkedList()
l3.build(5, 6)
l4 = LinkedList()
l4.build(7, 8)
merged = Solution.merge([l1, l2, l3, l4])
merged.show()

# Example 2
l1 = LinkedList()
l1.build(1, 3)
l2 = LinkedList()
l2.build(4, 5, 6)
l3 = LinkedList()
l3.build(8)
merged = Solution.merge([l1, l2, l3])
merged.show()

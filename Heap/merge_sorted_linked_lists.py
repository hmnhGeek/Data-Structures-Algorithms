from typing import List


class MinHeap:
    def __init__(self):
        self.heap = []

    def get_lci(self, pi):
        if pi is None: return
        lci = 2 * pi + 1
        return lci if lci in range(len(self.heap)) else None

    def get_rci(self, pi):
        if pi is None: return
        rci = 2 * pi + 2
        return rci if rci in range(len(self.heap)) else None

    def get_pi(self, ci):
        if ci == 0 or ci is None: return
        pi = int((ci - 1) / 2)
        return pi if pi in range(len(self.heap)) else None

    def get_min_child_index(self, lci, rci):
        if lci is None and rci is None: return None
        if lci is None: return rci
        if rci is None: return lci

        min_child_index = lci
        if self.heap[min_child_index][0] > self.heap[rci][0]:
            min_child_index = rci

        return min_child_index

    def min_heapify_up(self, start_index):
        pi = self.get_pi(start_index)
        if pi is None: return
        lci, rci = self.get_lci(pi), self.get_rci(pi)
        min_child_index = self.get_min_child_index(lci, rci)

        if min_child_index is not None:
            if self.heap[pi][0] > self.heap[min_child_index][0]:
                self.heap[pi], self.heap[min_child_index] = self.heap[min_child_index], self.heap[pi]
            self.min_heapify_up(pi)

    def min_heapify_down(self, pi):
        lci, rci = self.get_lci(pi), self.get_rci(pi)
        min_child_index = self.get_min_child_index(lci, rci)

        if min_child_index is not None:
            if self.heap[pi][0] > self.heap[min_child_index][0]:
                self.heap[pi], self.heap[min_child_index] = self.heap[min_child_index], self.heap[pi]
            self.min_heapify_down(min_child_index)

    def insert(self, x, node):
        self.heap.append([x, node])
        self.min_heapify_up(len(self.heap) - 1)

    def pop(self):
        N = len(self.heap)
        if N == 0: return

        self.heap[0], self.heap[N - 1] = self.heap[N - 1], self.heap[0]
        item = self.heap[N - 1]
        del self.heap[N - 1]
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

    def push(self, x):
        node = Node(x)

        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node

        self.length += 1

    def insert(self, x):
        # if the list is empty, simply push the item
        if self.head is None:
            self.push(x)

        # if x is even smaller than head, update head and insert x
        elif x <= self.head.data:
            node = Node(x)
            node.next = self.head
            self.head = node
            self.length += 1
        else:
            # case when x lies somewhere between or at the very end
            prev, curr = None, self.head
            node = Node(x)

            while curr is not None:
                # prev should be not None, because we have handled the case
                # when prev could be None in elif case
                if prev and prev.data < x <= curr.data:
                    # insert x between prev and curr
                    prev.next = node
                    node.next = curr

                prev = curr
                curr = curr.next

            # if x came out to be largest, insert x at end and update the tail value
            if curr is None and prev is not None and x > prev.data:
                prev.next = node
                self.tail = node

            self.length += 1

    def pop(self):
        if self.head is None: return
        node = self.head
        item = node.data
        self.head = self.head.next
        del node
        self.length -= 1
        return item

    def show(self):
        curr = self.head
        while curr is not None:
            print(curr.data, end=" ")
            curr = curr.next


def merge_sorted_linked_lists(l: List[LinkedList]) -> LinkedList:
    '''
        Overall time complexity is O(n * k * log(k))
        Overall space complexity is O(k)
    '''
    h = MinHeap()
    result = LinkedList()

    # inserting the first nodes form all the linked lists
    # takes O(k) time
    for ll in l:
        # takes O(log(k)) time
        h.insert(ll.head.data, ll.head)

    # overall till now, time complexity is O(k*log(k))

    # this loop will run for n*k times, as there are n*k nodes in total
    while len(h.heap) != 0:
        # takes log(k) to pop
        data, node = h.pop()

        # takes O(1) to push, note that instead of `insert` method
        # we are using `push` now, which simply appends.
        result.push(data)

        # takes another O(log(k)) to insert into heap
        if node.next is not None: h.insert(node.next.data, node.next)

    # overall time complexity till now O(nk log(k) + k log(k)) which is O(nk log(k))

    result.show()


def example1():
    l1 = LinkedList()
    l1.insert(1)
    l1.insert(2)
    l1.insert(3)

    l2 = LinkedList()
    l2.insert(4)
    l2.insert(5)

    l3 = LinkedList()
    l3.insert(5)
    l3.insert(6)

    l4 = LinkedList()
    l4.insert(7)
    l4.insert(8)

    L = [l1, l2, l3, l4]
    result = merge_sorted_linked_lists(L)


def example2():
    l1 = LinkedList()
    l1.insert(1)
    l1.insert(3)

    l2 = LinkedList()
    l2.insert(4)
    l2.insert(5)
    l2.insert(6)

    l3 = LinkedList()
    l3.insert(8)

    return merge_sorted_linked_lists([l1, l2, l3])


example1()
print()
example2()

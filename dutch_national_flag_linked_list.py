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

    def get_parent(self, node):
        curr = self.head
        prev = None

        while curr is not None:
            if curr == node:
                return prev
            prev = curr
            curr = curr.next

        return None

    def swap(self, node1, node2):
        # find the previous nodes
        parent1, parent2 = self.get_parent(node1), self.get_parent(node2)

        # update the heads, if required
        if node1 == self.head:
            self.head = node2
        elif node2 == self.head:
            self.head = node1

        # handle the parent pointers
        if parent1 is not None:
            parent1.next = node2
        if parent2 is not None:
            parent2.next = node1

        # swap next pointers
        # Adjacent nodes
        if node1.next == node2:
            node1.next = node2.next
            node2.next = node1
        elif node2.next == node1:
            node2.next = node1.next
            node1.next = node2
        else:
            temp = node1.next
            node1.next = node2.next
            node2.next = temp

        # handle the tail nodes, if needed
        if node1 == self.tail:
            self.tail = node2
        elif node2 == self.tail:
            self.tail = node1

    def show(self):
        curr = self.head
        while curr is not None:
            print(curr.data, end=" ")
            curr = curr.next


def dutch_sort(l: LinkedList):
    low = l.head
    mid = l.head
    high = l.tail

    # read as mid < high
    while high.next != mid:
        if mid.data == 0:
            l.swap(low, mid)

            keep_track_of_high = False
            if high == mid:
                keep_track_of_high = True
            low, mid = mid, low
            if keep_track_of_high:
                high = mid

            low = low.next
            mid = mid.next

        elif mid.data == 1:
            mid = mid.next

        elif mid.data == 2:
            l.swap(mid, high)

            keep_track_of_low = False
            if low == mid:
                keep_track_of_low = True
            mid, high = high, mid
            if keep_track_of_low:
                low = mid
            high = l.get_parent(high)


def example1():
    l = [1, 2, 2, 1, 2, 0, 2, 2]
    L = LinkedList()

    for i in l:
        L.push(i)

    dutch_sort(L)
    L.show()


def example2():
    l = [2, 2, 0, 1]
    L = LinkedList()

    for i in l:
        L.push(i)

    dutch_sort(L)
    L.show()


example1()
print()
example2()
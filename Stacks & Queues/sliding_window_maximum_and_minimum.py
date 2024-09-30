# Problem link - https://www.geeksforgeeks.org/sum-minimum-maximum-elements-subarrays-size-k/
# Solution - https://www.youtube.com/watch?v=CZQGRp93K4k


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = self.tail = None
        self.length = 0

    def is_empty(self):
        return self.length == 0

    def get_front(self):
        if self.is_empty():
            return
        return self.head.data

    def get_back(self):
        if self.is_empty():
            return
        return self.tail.data

    def push_front(self, x):
        node = Node(x)
        if self.is_empty():
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.length += 1

    def pop_front(self):
        if self.is_empty():
            return
        item = self.head.data
        node = self.head
        self.head = self.head.next
        if self.head is not None:
            self.head.prev = None
        del node
        self.length -= 1
        return item

    def push_back(self, x):
        node = Node(x)
        if self.is_empty():
            self.head = self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.length += 1

    def pop_back(self):
        if self.is_empty():
            return
        item = self.tail.data
        node = self.tail
        self.tail = self.tail.prev
        if self.tail is not None:
            self.tail.next = None
        del node
        self.length -= 1
        return item

    def show(self):
        curr = self.head
        while curr is not None:
            print(curr.data, end=" ")
            curr = curr.next
        print()


def get_sliding_window_maximum(arr, k):
    """
        Time complexity is O(n) and space complexity O(k).
    """

    n = len(arr)

    # create a doubly linked list instance for using it as a deque.
    doubly_linked_list = DoublyLinkedList()

    # create a doubly linked list instance for storing the max results.
    result = DoublyLinkedList()

    # iterate on all the indices of the array.
    for i in range(n):
        # if from the front side, there is an index (i - k) which is out of window from the left side,
        # pop from the front side.
        if not doubly_linked_list.is_empty() and doubly_linked_list.get_front() == i - k:
            doubly_linked_list.pop_front()

        # while the deque is not empty and from the back side, if the elements are <= current ith element,
        # then continuously pop from back side. This will ensure that deque will store elements in decreasing
        # order, so that the max lies in the front always.
        while not doubly_linked_list.is_empty() and arr[doubly_linked_list.get_back()] <= arr[i]:
            doubly_linked_list.pop_back()

        # push the current index from the back side.
        doubly_linked_list.push_back(i)

        # if you've crossed the first window, start pushing the front to the result because front element is
        # the max element.
        if i >= k - 1:
            result.push_back(arr[doubly_linked_list.get_front()])

    # return the doubly linked list `result`.
    return result


def get_sliding_window_minimum(arr, k):
    """
        Time complexity is O(n) and space complexity O(k).
    """

    n = len(arr)

    # create a doubly linked list instance for using it as a deque.
    doubly_linked_list = DoublyLinkedList()

    # create a doubly linked list instance for storing the max results.
    result = DoublyLinkedList()

    # iterate on all the indices of the array.
    for i in range(n):
        # if from the front side, there is an index (i - k) which is out of window from the left side,
        # pop from the front side.
        if not doubly_linked_list.is_empty() and doubly_linked_list.get_front() == i - k:
            doubly_linked_list.pop_front()

        # while the deque is not empty and from the back side, if the elements are <= current ith element,
        # then continuously pop from back side. This will ensure that deque will store elements in decreasing
        # order, so that the max lies in the front always.
        while not doubly_linked_list.is_empty() and arr[doubly_linked_list.get_back()] >= arr[i]:
            doubly_linked_list.pop_back()

        # push the current index from the back side.
        doubly_linked_list.push_back(i)

        # if you've crossed the first window, start pushing the front to the result because front element is
        # the max element.
        if i >= k - 1:
            result.push_back(arr[doubly_linked_list.get_front()])

    # return the doubly linked list `result`.
    return result


def sum_min_max(arr, k):
    # Time complexity is O(n) and space complexity is O(k).

    result1 = get_sliding_window_maximum(arr, k)
    result2 = get_sliding_window_minimum(arr, k)
    curr1 = result1.head
    curr2 = result2.head
    result = 0

    while curr1 is not None:
        result += (curr1.data + curr2.data)
        curr1 = curr1.next
        curr2 = curr2.next

    return result


print(sum_min_max([2, 5, -1, 7, -3, -1, -2], 4))
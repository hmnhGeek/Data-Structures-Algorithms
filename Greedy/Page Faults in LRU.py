# Problem link - https://www.geeksforgeeks.org/problems/page-faults-in-lru5603/1
# Explanation Video - https://www.youtube.com/watch?v=dYIoWkCvd6A


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

    def get_node(self, x):
        curr = self.head
        while curr is not None:
            if curr.data == x:
                return curr
            curr = curr.next
        return None

    def move_back(self, node):
        temp = node.data
        curr = node
        while curr.next is not None:
            curr.data = curr.next.data
            curr = curr.next
        curr.data = temp

    def pop_front(self):
        if self.is_empty():
            return
        item = self.head.data
        self.head = self.head.next
        self.length -= 1
        return item

    def __len__(self):
        return self.length


class Solution:
    @staticmethod
    def get_page_faults(arr, cap):
        """
            Time complexity is O(n * c), why c and not `n`? Because moving back in the queue only takes a traversal of
            the queue, which will be of `c` length.

            Space complexity is O(c).
        """

        queue = LinkedList()
        page_faults = 0
        n = len(arr)

        # loop on the pages
        for i in range(n):
            # extract the node with value arr[i]...
            node = queue.get_node(arr[i])

            # now check if queue has capacity or not...
            if len(queue) < cap:
                # if it has capacity and the node extracted is None
                if node is None:
                    # there's a page fault, push the arr[i] element.
                    queue.push(arr[i])
                    page_faults += 1
                else:
                    # else, make this node most recently used, thus moving it to last.
                    queue.move_back(node)
            elif node is None:
                # if this node is found and queue is full, pop the LRU and push this node to back as MRU.
                queue.pop_front()
                queue.push(arr[i])
                page_faults += 1
            else:
                # else, make this node most recently used, thus moving it to last.
                queue.move_back(node)
        return page_faults


print(Solution.get_page_faults([5, 0, 1, 3, 2, 4, 1, 0, 5], 4))
print(Solution.get_page_faults([1, 2, 1, 4, 2, 3, 5], 3))
print(Solution.get_page_faults([5, 0, 1, 3, 2], 3))

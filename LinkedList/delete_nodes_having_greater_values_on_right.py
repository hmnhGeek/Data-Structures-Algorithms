# Problem link - https://www.geeksforgeeks.org/problems/delete-nodes-having-greater-value-on-right/1


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

    def reverse(self):
        # Standard reverse function in O(N) time and O(1) space.
        curr = self.head
        prev = None
        while curr is not None:
            next_curr = curr.next
            curr.next = prev
            prev = curr
            curr = next_curr
        self.head, self.tail = self.tail, self.head

    def flatten(self):
        """
            The idea is to reverse the linked list first and then iterate on it in such a way
            that at any node, if it's data is less than max till now, delete this node, else
            keep moving.

            This will take O(3N) time and O(1) space.
        """

        # Reverse in O(N) time.
        self.reverse()

        # Please note that the head of this reversed linked list (or the tail of the original list)
        # will never be deleted.

        # store -inf as max till now.
        max_data = float('-inf')

        # start iterating on the reversed list
        prev, curr = None, self.head
        while curr is not None:
            # if the current node's data is less than the max till now, then we must delete the
            # current node. Point prev's next to curr's next and if the curr node that is being
            # deleted is a tail node, then update the tail to prev.
            if curr.data < max_data:
                if prev is not None:
                    prev.next = curr.next
                if curr == self.tail:
                    self.tail = prev

            # else if we get a new maximum value, then update that value and simply update prev to
            # curr node.
            elif max_data < curr.data:
                max_data = curr.data
                prev = curr
            else:
                # if the max value and current node's data is same, simply move ahead
                prev = curr

            # move to next curr
            curr = curr.next

        # finally reverse the list again in O(N).
        self.reverse()

    def show(self):
        curr = self.head
        while curr is not None:
            print(curr.data, end=" ")
            curr = curr.next
        print()


def test(example_list):
    l = LinkedList()
    for i in example_list:
        l.push(i)
    l.show()
    l.flatten()
    l.show()
    print()


test([12, 15, 10, 11, 5, 6, 2, 3])

test([10, 20, 30, 40, 50, 60])

test([8, 7, 8, 4, 5, 6, 2, 1, -1])

test([6, 5, 3, 2, 1, -1])

test([10, 8, 7, 12, 5, -1])

test([5, 6, 7, 8, 10, 12, -1])

test([5, 2, 13, 3, 8])

test([1, 1, 1, 1])

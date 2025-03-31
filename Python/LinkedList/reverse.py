# Problem link - https://www.geeksforgeeks.org/reverse-a-linked-list/


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = self.tail = None
        self.length = 0

    def build(self, l):
        for i in l:
            self.push(i)

    def push(self, x):
        node = Node(x)
        if self.length == 0:
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

    def reverse(self):
        """
            Time complexity is O(n) and space complexity is O(1).
        """

        # start with blank prev and curr pointing to head.
        prev, curr = None, self.head
        # start traversing the whole list.
        while curr is not None:
            # store the next curr that should be updated in the next iteration.
            next_curr = curr.next
            # make curr's next point to prev (reversed the link here).
            curr.next = prev
            # update the prev pointer to curr.
            prev = curr
            # update the curr pointer to next curr.
            curr = next_curr
        # finally swap the head and tail nodes to complete the reversal.
        self.head, self.tail = self.tail, self.head

    def recursive_reverse(self, prev, curr):
        """
            Time complexity would be O(n) and space complexity would be O(n) for the recursion stack.
        """

        # prev will be None for the first time only.
        if prev is None:
            # set the tail pointer to point to curr which is head (i.e., first curr value).
            self.tail = curr

        # curr will be None when entire list is traversed.
        if curr is None:
            # the prev should now point to the head.
            self.head = prev
            # return from the recursion stack.
            return

        # store the next curr value.
        next_curr = curr.next
        # reverse the current link between curr and prev.
        curr.next = prev
        # recursively call this method with prev as curr and curr and next_curr.
        self.recursive_reverse(curr, next_curr)


def test_iterative(l):
    print("\nTesting iterative reverse method.")
    linked_list = LinkedList()
    linked_list.build(l)
    print("Original List:")
    linked_list.show()
    linked_list.reverse()
    print("Reversed List:")
    linked_list.show()


def test_recursive(l):
    print("\nTesting recursive reverse method.")
    linked_list = LinkedList()
    linked_list.build(l)
    print("Original List:")
    linked_list.show()
    linked_list.recursive_reverse(None, linked_list.head)
    print("Reversed List:")
    linked_list.show()


test_iterative([1, 2, 3, 4, 5])
test_recursive([1, 2, 3, 4, 5])
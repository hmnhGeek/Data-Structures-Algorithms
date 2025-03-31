# Problem link - https://leetcode.com/problems/middle-of-the-linked-list/description/


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = self.tail = None

    def show(self):
        curr = self.head
        while curr is not None:
            print(curr.data, end=" --> ")
            curr = curr.next
        print()

    def find_middle(self):
        # In O(n/2) time, we get the middle node.
        slow = fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow.data

    """ Using the builder pattern to construct the linked list, while the core functionalities
        of the linked list are in the class LinkedList. """
    class Builder:
        def __init__(self):
            self.head = self.tail = None

        def add(self, x):
            node = Node(x)
            if self.head is None:
                self.head = self.tail = node
            else:
                self.tail.next = node
                self.tail = node
            return self

        def build(self):
            linked_list = LinkedList()
            linked_list.head = self.head
            linked_list.tail = self.tail
            return linked_list


# Example 1
l1 = LinkedList.Builder() \
    .add(1) \
    .add(2) \
    .add(3) \
    .add(4) \
    .add(5) \
    .build()
l1.show()
print(l1.find_middle())

l2 = LinkedList.Builder() \
    .add(1) \
    .add(2) \
    .add(3) \
    .add(4) \
    .add(5) \
    .add(6) \
    .build()
l2.show()
print(l2.find_middle())
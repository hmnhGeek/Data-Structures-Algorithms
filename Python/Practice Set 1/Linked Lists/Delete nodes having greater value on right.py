# Problem link - https://leetcode.com/problems/remove-nodes-from-linked-list/description/


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

    def build(self, *args):
        for i in args:
            self.push(i)

    def show(self):
        curr = self.head
        while curr is not None:
            print(curr.data, end=" ")
            curr = curr.next
        print()

    def reverse(self):
        prev, curr = None, self.head
        while curr is not None:
            next_curr = curr.next
            curr.next = prev
            prev = curr
            curr = next_curr
        self.head, self.tail = self.tail, self.head


class Solution:
    @staticmethod
    def delete(l: LinkedList):
        """
            Overall time complexity is O(n) and space complexity is O(n).
        """

        # first reverse the linked list in O(n) time.
        l.reverse()

        # start with prev and curr pointers. Note that head, i.e., prev pointer will never be deleted because it is the
        # node from which the comparison is starting.
        prev, curr = l.head, l.head.next

        # standard O(n) linked list traversal.
        while curr is not None:
            # if in this reversed list, the next node to prev, i.e., curr is smaller, then delete the curr node because
            # in the original question, we have to delete node which has something greater on the right.
            if curr.data < prev.data:
                prev.next = curr.next
                temp = curr
                # edge case: if the deleted node is a tail node, update the tail to prev node.
                if temp == l.tail:
                    l.tail = prev
                del temp
                l.length -= 1
            else:
                prev = curr
            curr = curr.next

        # ensure to revert back to original order in O(n) time.
        l.reverse()


l1 = LinkedList()
l1.build(10, 20, 30, 40, 50, 60)
l1.show()
Solution.delete(l1)
l1.show()

l2 = LinkedList()
l2.build(12, 15, 10, 11, 5, 6, 2, 3)
l2.show()
Solution.delete(l2)
l2.show()

l3 = LinkedList()
l3.build(5, 2, 13, 3, 8)
l3.show()
Solution.delete(l3)
l3.show()

l4 = LinkedList()
l4.build(1, 1, 1, 1)
l4.show()
Solution.delete(l4)
l4.show()

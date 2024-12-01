# Problem link - https://www.geeksforgeeks.org/problems/check-if-linked-list-is-pallindrome/1
# Solution - https://www.youtube.com/watch?v=lRY_G-u_8jk


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = self.tail = None

    def _push(self, x):
        node = Node(x)
        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def build(self, *args):
        for i in args:
            self._push(i)

    def show(self):
        curr = self.head
        while curr is not None:
            print(curr.data, end=" ")
            curr = curr.next
        print()

    def reverse(self):
        prev = None
        curr = self.head
        while curr is not None:
            next_curr = curr.next
            curr.next = prev
            prev = curr
            curr = next_curr
        self.head, self.tail = self.tail, self.head

    def get_middle_node(self):
        slow = self.head
        fast = slow.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def is_palindrome(self):
        """
            Overall time complexity is O(n) and space complexity is O(1).
        """

        # get the middle node of the linked list in O(n) time.
        middle_node = self.get_middle_node()

        # for the next half, the head will be middle node's next.
        next_head = middle_node.next

        # break the first half and second half.
        middle_node.next = None

        # build first half linked list
        l1 = LinkedList()
        l1.head = self.head
        l1.tail = middle_node

        # build second half linked list
        l2 = LinkedList()
        l2.head = next_head
        l2.tail = self.tail

        # reverse the second half linked list for checking palindrome. Another O(n) time.
        l2.reverse()

        # traverse on left and right half until second half is exhausted. This will take
        # O(n) time.
        curr1, curr2 = l1.head, l2.head
        palindrome = True
        while curr2 is not None:
            # if at any point, the data do not match, set palindrome to false.
            if curr1.data != curr2.data:
                palindrome = False
            curr1 = curr1.next
            curr2 = curr2.next

        # once palindrome flag is updated, reverse back second half. Another O(n) time.
        l2.reverse()

        # link back the halves to restore original list
        l1.tail.next = l2.head

        # return palindrome flag
        return palindrome


def test(*args):
    l = LinkedList()
    l.build(*args)
    l.show()
    print(l.is_palindrome())
    l.show()
    print()


test(1, 2, 2, 1)
test(1, 2, 3, 4)
test(1, 2, 3, 2, 1)
test(1, 2, 3, 4, 1)
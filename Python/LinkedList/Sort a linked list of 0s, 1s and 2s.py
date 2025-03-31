# Problem link - https://www.geeksforgeeks.org/sort-a-linked-list-of-0s-1s-or-2s/
# Solution - https://www.youtube.com/watch?v=gRII7LhdJWc&t=1214s


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

    def show(self):
        curr = self.head
        while curr is not None:
            print(curr.data, end=" ")
            curr = curr.next
        print()


class Solution:
    @staticmethod
    def sort(l: LinkedList):
        """
            Time complexity is O(n) and space complexity is O(1).
        """

        # create head and temp nodes, where head's next will be used to determine the beginning of a sublist.
        zero_head = zero_temp = Node(None)
        one_head = one_temp = Node(None)
        two_head = two_temp = Node(None)

        # variables to check if 0, 1 and 2 have been found or not.
        zero_found = one_found = two_found = False

        # traverse on the list
        curr = l.head
        while curr is not None:
            # if curr is 0
            if curr.data == 0:
                # set zero found to true
                zero_found = True
                # add this 0 node to zero sublist
                zero_temp.next = curr
                zero_temp = curr
            elif curr.data == 1:
                one_found = True
                # add this 1 node to zero sublist
                one_temp.next = curr
                one_temp = curr
            else:
                two_found = True
                # add this 2 node to zero sublist
                two_temp.next = curr
                two_temp = curr
            curr = curr.next

        # since 1 acts as a bridge between 0 and 2, we must explicitly check for its presence.
        if one_found:
            zero_temp.next = one_head.next
            one_temp.next = two_head.next
        else:
            # else directly connect 0 sublist to 2 sublist.
            zero_temp.next = two_head.next

        # decide which sublist's start will act has the new head
        if zero_found:
            l.head = zero_head.next
        elif one_found:
            l.head = one_head.next
        else:
            l.head = two_head.next

        # decide which sublist's last node will act as the new tail.
        if two_found:
            l.tail = two_temp
        elif one_found:
            l.tail = one_temp
        else:
            l.tail = zero_temp

        # ensure tail points to None.
        if l.tail:
            l.tail.next = None


l = LinkedList()
for i in [1, 2, 2, 1, 2, 0, 2, 2]:
    l.push(i)
l.show()
Solution.sort(l)
l.show()

print()

l2 = LinkedList()
for i in [2, 2, 0, 1]:
    l2.push(i)
l2.show()
Solution.sort(l2)
l2.show()

print()
l3 = LinkedList()
for i in [1, 1, 2, 0, 2, 0, 1]:
    l3.push(i)
l3.show()
Solution.sort(l3)
l3.show()

print()
l4 = LinkedList()
for i in [1, 1, 2, 1, 2, 2, 1]:
    l4.push(i)
l4.show()
Solution.sort(l4)
l4.show()

print()
l5 = LinkedList()
for i in [0, 2, 2, 2, 0, 0, 0, 0, 2, 2]:
    l5.push(i)
l5.show()
Solution.sort(l5)
l5.show()

print()
l6 = LinkedList()
for i in [0, 1, 1, 1, 0, 0, 0, 0, 1, 1]:
    l6.push(i)
l6.show()
Solution.sort(l6)
l6.show()

print()
l7 = LinkedList()
for i in [0, 0, 0, 0, 0]:
    l7.push(i)
l7.show()
Solution.sort(l7)
l7.show()

print()
l8 = LinkedList()
for i in [1, 1, 1, 1, 1, 1]:
    l8.push(i)
l8.show()
Solution.sort(l8)
l8.show()

print()
l9 = LinkedList()
for i in [2, 2, 2, 2, 2]:
    l9.push(i)
l9.show()
Solution.sort(l9)
l9.show()

print()
l10 = LinkedList()
for i in []:
    l10.push(i)
l10.show()
Solution.sort(l10)
l10.show()

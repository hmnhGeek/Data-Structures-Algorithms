# Problem link - https://www.geeksforgeeks.org/problems/remove-duplicates-from-an-unsorted-linked-list/1


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
        if self.length == 0:
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
        print()

    def delete(self, prev, node):
        """
            This is a O(1) time complexity and O(1) space complexity method.
        """
        # if the node to be deleted is head node
        if prev is None and node == self.head:
            self.head = self.head.next
            return

        # check if prev's next is node only or not
        if prev.next != node:
            return

        # if node to be deleted is tail node
        elif node == self.tail:
            prev.next = None
            self.tail = prev

        # else delete the node simply.
        else:
            prev.next = node.next
        del node
        self.length -= 1

    def remove_duplicates(self):
        """
            Overall time complexity is O(n) and overall space complexity is O(n) for hash map and second occurence dict,
            assuming all the nodes are unique in the worst case.
        """

        # create a hash map to store the count of each data node.
        hash_map = {}

        # create a hash map to signify if the data node has been seen for the second time or not.
        second_occur = {}

        # loop on the linked list now. This will take O(n) time.
        curr = self.head
        while curr is not None:
            # set the second occurence to false, meaning that for now we are assuming that this node has not been seen
            # at all, let alone being seen second time.
            second_occur[curr.data] = False

            # store the counter value of data node in hash map
            if curr.data not in hash_map:
                hash_map[curr.data] = 1
            else:
                hash_map[curr.data] += 1
            curr = curr.next

        # now loop on the linked list again in O(n) time.
        prev, curr = None, self.head
        while curr is not None:
            # if the current node's data has a frequency of more than 1, and it is being encountered after the 1st
            # occurence, then delete this node.
            if hash_map[curr.data] > 1 and second_occur[curr.data]:
                # store the reference to next current
                temp = curr.next
                # delete the node in O(1) time.
                self.delete(prev, curr)
                # decrement the frequency of this node.
                hash_map[curr.data] -= 1
                # update curr and keep prev the same.
                curr = temp

            # else if the current node's data has a frequency of more than 1, and it is being encountered for the first
            # time, then...
            elif hash_map[curr.data] > 1 and not second_occur[curr.data]:
                # simply set the flag for the second occurence to be true and do not delete this node.
                second_occur[curr.data] = True
                prev = curr
                curr = curr.next
            else:
                # else if the current node has exactly 1 frequency count, nothing needs to be done.
                prev = curr
                curr = curr.next


l1 = LinkedList()
l1.build(5, 2, 2, 4)
l1.show()
l1.remove_duplicates()
l1.show()

l2 = LinkedList()
l2.build(2, 2, 2, 2, 2)
l2.show()
l2.remove_duplicates()
l2.show()

l3 = LinkedList()
l3.build(12, 11, 12, 21, 41, 43, 21)
l3.show()
l3.remove_duplicates()
l3.show()

l4 = LinkedList()
l4.build(1, 2, 3, 2, 4)
l4.show()
l4.remove_duplicates()
l4.show()

l5 = LinkedList()
l5.build(4, 2, 5, 4, 2, 2, -1)
l5.show()
l5.remove_duplicates()
l5.show()

l6 = LinkedList()
l6.build(1, 2, 1, 2, 2, 2, 7, 7, -1)
l6.show()
l6.remove_duplicates()
l6.show()

l7 = LinkedList()
l7.build(3, 3, 3, 3, 3, -1)
l7.show()
l7.remove_duplicates()
l7.show()

l8 = LinkedList()
l8.build(10, 20, 10, 20, 30, 10, 20, 30, -1)
l8.show()
l8.remove_duplicates()
l8.show()
# Problem link - https://www.naukri.com/code360/problems/reverse-list-in-k-groups_983644
# Solution - https://www.youtube.com/watch?v=lIar1skcQYI

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = self.tail = None

    def push(self, x: int):
        node = Node(x)

        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def reverse(self):
        # standard reversing approach in O(N) time to reverse a linked list
        prev = None
        curr = self.head

        while curr is not None:
            # store the next curr reference
            next_curr = curr.next
            # revert the next pointer to point to prev
            curr.next = prev
            # update the prev pointer to the curr node
            prev = curr
            # switch to next curr
            curr = next_curr

        # swap head and tail pointers
        self.head, self.tail = self.tail, self.head

    def _get_kth_node(self, start_node, k):
        # Time complexity is O(N)

        # point curr to the starting node
        curr = start_node
        # store a prev pointer as this will be useful when k is out of bounds
        prev = None
        # store the counter = 1 as you are standing on the first node
        counter = 1

        while curr is not None:
            # if counter is same as k, then it means you are on the kth node, return curr
            if counter == k:
                return curr

            # otherwise store curr in prev and point curr to its next
            prev = curr
            curr = curr.next

            # increment the counter as you've moved to the next node
            counter += 1

        # in any case, if you were not able to reach kth node, i.e., loop finished
        # before counter reached k, then you can simply return the last node.
        return prev

    def reverse_in_parts(self, num_parts):
        # To reverse in parts, the idea is to separate k units of linked list,
        # reverse it, and join it back in the original list. This whole operation
        # would also take O(N) time.

        # start by storing prev and curr pointers
        curr = self.head
        prev = None

        while curr is not None:
            # get the kth node from curr
            kth_node = self._get_kth_node(curr, num_parts)
            # store the next curr for next while loop iteration as we are going to break
            # the list after kth node in next statement.
            next_curr = kth_node.next
            # break the list at kth node
            kth_node.next = None

            # if prev is None, then it means that you are on the first part. After reversing
            # this part, head of the original list will actually point to the kth node.
            if prev is None:
                self.head = kth_node

            # create a temporary linked list out of the extracted part and reverse it.
            temp_linked_list = LinkedList()
            temp_linked_list.head = curr
            temp_linked_list.tail = kth_node
            temp_linked_list.reverse()

            # if prev node is not None, then you can simply assign prev's next pointer to
            # the kth node, which is now the first node after reversing the part. Basically,
            # this is relinking of the part into the original list.
            if prev is not None:
                prev.next = kth_node

            # curr has become the last node of the part, update prev pointer to curr, as this
            # will be the prev for the next iteration
            prev = curr
            # update curr to next_curr which we stored already
            curr = next_curr

        # update the tail pointer of the original list because prev would be storing the last
        # node of the last reversed part.
        self.tail = prev

    def show(self):
        curr = self.head
        while curr is not None:
            print(curr.data, end=" ")
            curr = curr.next
        print()

    def build(self, _list):
        for i in _list:
            self.push(i)


l1 = LinkedList()
l1.build([1, 2, 3, 4, 5, 6, 7, 8])
l1.show()
l1.reverse_in_parts(3)
l1.show()

print()
l2 = LinkedList()
l2.build([1, 2, 3, 4, 5, 6, 7, 8])
l2.show()
l2.reverse_in_parts(5)
l2.show()

print()
l3 = LinkedList()
l3.build([1, 2, 3, 4, 5])
l3.show()
l3.reverse_in_parts(2)
l3.show()

print()
l4 = LinkedList()
l4.build([1, 2, 3, 4, 5])
l4.show()
l4.reverse_in_parts(3)
l4.show()
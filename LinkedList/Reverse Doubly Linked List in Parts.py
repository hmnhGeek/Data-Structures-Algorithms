class Node:
    def __init__(self, data):
        self.data = data
        self.prev = self.next = None


class DoublyLinkedList:
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
            node.prev = self.tail
            self.tail = node
        self.length += 1

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
            curr.prev = next_curr
            prev = curr
            curr = next_curr
        self.head, self.tail = self.tail, self.head

    def _get_kth_node(self, prev, start_node, k):
        """
            Time complexity is O(n) and space complexity is O(1).
        """

        counter = 1
        prev = None
        while counter != k and start_node is not None:
            prev = start_node
            start_node = start_node.next
            counter += 1
        if start_node is None:
            return prev
        return start_node

    def reverse_in_parts(self, k):
        """
            Overall, the while loop runs for the entire DLL but in hops. Within each hop, there is a O(k) iteration.
            Overall, this becomes O(n) time complexity and O(1) space for each sub-list (as no new nodes are created for
            each sublist).
        """

        # if k is exactly the same as the length of the linked list, simply reverse the whole list
        if k == self.length:
            self.reverse()
            return

        # if k is 0 or negative, return, do nothing.
        if k <= 0:
            return

        # initialize start_node and curr to head. Remember, start_node will always stay where it is, curr will move.
        start_node = curr = self.head

        # last node will represent the tail of the last sub-list that was reversed. Initially, it is None.
        last_node = None

        # now start the traversal on the list.
        while curr is not None:
            # get the kth node of the list in O(k) time, starting from curr node.
            kth_node = self._get_kth_node(None, curr, k)

            # store the head of the next list that will be reversed in the next iteration.
            temp = kth_node.next

            # break the linkage between temp and kth node.
            kth_node.next = None
            if temp is not None:
                temp.prev = None

            # create a sub-list from start_node till kth node and reverse this part in O(k) time.
            sub_dll = DoublyLinkedList()
            sub_dll.head = start_node
            sub_dll.tail = kth_node
            sub_dll.reverse()

            # if there was some last list which was reversed...
            if last_node is not None:
                # then the last node's next should point to the kth node (remember, kth node has come to front after the
                # reversal).
                last_node.next = kth_node
                # and kth node's prev should point to this last node.
                kth_node.prev = last_node
            else:
                # else this was the first sub list to be reversed; therefore, the kth node will be the head of the
                # complete DLL.
                self.head = kth_node

            # if there is no next sub-list to reverse...
            if temp is None:
                # then the start node (which has come to the last after sub-list reversal) will be the tail of the whole
                # DLL.
                self.tail = start_node

            # finally, update the last node to the start node of this DLL (start node has become the last node of this
            # sub-list).
            last_node = start_node

            # move curr and start node to temp.
            curr = start_node = temp


def test(*args):
    k = args[-1]
    n = len(args)
    dll = DoublyLinkedList()
    for i in range(n - 1):
        dll.push(args[i])
    dll.show()
    dll.reverse_in_parts(k)
    dll.show()


test(1, 2, 3, 4, 5, 6, 4)
test(1, 2, 3, 4, 5, 6, 2)
test(1, 2, 3, 4, 5, 2)
test(1, 2, 3, 4, 5, 3)
test(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 3)
test(5, 4, 3, 7, 9, 2, 4)

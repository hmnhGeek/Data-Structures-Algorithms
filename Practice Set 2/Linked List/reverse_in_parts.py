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

        prev, curr = None, self.head
        while curr is not None:
            next_curr = curr.next
            curr.next = prev
            prev = curr
            curr = next_curr
        self.head, self.tail = self.tail, self.head

    def get_kth_node(self, curr, k):
        if k == 1:
            return curr
        counter = 1
        while curr.next is not None:
            curr = curr.next
            counter += 1
            if counter == k:
                return curr
        return curr

    def build(self, *args):
        for i in args:
            self.push(i)

    def reverse_in_parts(self, k):
        # To reverse in parts, the idea is to separate k units of linked list,
        # reverse it, and join it back in the original list. This whole operation
        # would also take O(N) time. Space complexity is O(k).

        if k <= 0:
            return
        if k >= self.length:
            self.reverse()
            return
        curr = self.head
        temp = None
        while curr is not None:
            # get the kth node in O(k) time.
            kth_node = self.get_kth_node(curr, k)

            # store the pointer to next current
            next_curr = kth_node.next

            # break the list at kth node.
            kth_node.next = None

            # create a sublist from curr to kth node and reverse it in O(k) time and O(k) space.
            sublist = LinkedList()
            sublist.head = curr
            sublist.tail = kth_node
            sublist.reverse()

            # if there was no previously reversed list, this first reversed list will have the new head.
            if temp is None:
                self.head = kth_node
            else:
                # else point the tail of previously reversed sublist's to current sublist's head.
                temp.next = sublist.head

            # update temp and curr.
            temp = curr
            curr = next_curr

        # update the tail of the whole list.
        self.tail = temp


def test(*args):
    l1 = LinkedList()
    l1.build(*args[:-1])
    l1.show()
    l1.reverse_in_parts(args[-1])
    l1.show()


test(1, 2, 3, 4, 5, 3)
test(1, 2, 2, 4, 5, 6, 7, 8, 4)
test(1, 2, 3, 4, 5, 2)
test(1, 2, 3, 4, 5, 6, 7, 8, 3)
test(1, 2, 3, 4, 5, 4)

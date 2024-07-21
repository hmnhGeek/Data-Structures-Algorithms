from typing import Any


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

    def get_prev(self, x: Node) -> Node | None:
        prev = None
        curr = self.head

        while curr is not None:
            if curr == x:
                return prev
            prev = curr
            curr = curr.next

        return None

    def push(self, x):
        node = Node(x)
        if self.is_empty():
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.length += 1

    def swap(self, x: Node, y: Node):
        prevX = self.get_prev(x)
        prevY = self.get_prev(y)

        # handle the head nodes
        if x == self.head:
            self.head = y
        elif y == self.head:
            self.head = y

        # handle the previous nodes
        if prevX is not None:
            prevX.next = y
        if prevY is not None:
            prevY.next = x

        # handle the swap now
        # if the nodes are adjacent
        if x.next == y:
            x.next = y.next
            y.next = x
        elif y.next == x:
            y.next = x.next
            x.next = y
        else:
            # nodes are not adjacent
            temp = x.next
            x.next = y.next
            y.next = temp

        # handle the tail node cases
        if x == self.tail:
            self.tail = x
        elif y == self.tail:
            self.tail = x

    def _show(self, start):
        if start:
            print(start.data, end=" ")
            self._show(start.next)

    def show(self):
        self._show(self.head)


def reverse_linked_list(head: Node) -> Node:
    # first of all get the tail node.
    curr = head
    while curr.next is not None:
        curr = curr.next

    # last node is tail
    tail = curr

    prev = None
    curr = head

    while curr is not None:
        next_curr = curr.next
        curr.next = prev
        prev = curr
        curr = next_curr

    # return tail which is now new head
    return tail


def get_kth_node(head, k):
    curr = head
    counter = 1

    while counter != k and curr.next is not None:
        curr = curr.next
        counter += 1

    return curr


def reverse_in_parts(ll, k: int):
    temp = ll.head
    prev = None

    while temp is not None:
        # find the kth node from temp node, which is a starting node
        kth_node = get_kth_node(temp, k)

        # if prev node is not None, then assign prev.next to kth_node
        # because in the next part, after reversing, kth_node will become
        # the first node
        if prev:
            prev.next = kth_node

        # store the next temp which would be the next node to kth_node
        # and delink the kth_node -> next_temp node link.
        # so now we have a part of the list from temp (start) to kth_node (end)
        next_temp = kth_node.next
        kth_node.next = None

        # take care of the edge case when temp is the head of the linked list,
        # i.e., we are on the first part. If this is true, kth_node will become the
        # new head of the list, update it.
        if temp == ll.head:
            ll.head = kth_node

        # reverse the current part starting at head
        reverse_linked_list(temp)

        # now head has become the last node,
        # update the prev to temp node so that in the next iteration,
        # we can link prev to the next kth_node (kth node of next part)
        prev = temp

        # update the temp to next temp which we stored.
        # this will be the starting node of next part.
        temp = next_temp

    # update the tail pointer
    # at this point, prev would hold the last node
    # in the final result. That should be the tail pointer.
    ll.tail = prev

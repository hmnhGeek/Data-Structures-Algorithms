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

    def build(self, _list):
        for i in _list:
            self.push(i)

    def show(self):
        curr = self.head
        while curr is not None:
            print(curr.data, end=" ")
            curr = curr.next
        print()


class LinkedListSplitter:
    def __init__(self, linked_list: LinkedList):
        self.linked_list = linked_list

    def split(self):
        # create a dummy node which will be useful to update the head of the linked list
        # once segregation is done. Point it's next pointer to the original head of the
        # linked list for now. Later, when an even node is prepended, at that time,
        # dummy_node.next will be updated to the first such even node and will never change.
        dummy_node = Node(None)
        dummy_node.next = self.linked_list.head

        # create a last node variable which will act as a tail pointer for segregated
        # even nodes which will be prepended in the front of the list. Basically, the
        # idea is to maintain the relative order of the even nodes even in the prepended
        # part. So, the last_node variable will always point to the last even node attached
        # before the head.
        last_node = None

        # create prev and curr pointers for linked list traversal.
        prev, curr = None, self.linked_list.head
        while curr is not None:
            # if the current node is not the original head, and it is an even node, then it must
            # be prepended.
            if curr != self.linked_list.head and curr.data % 2 == 0:
                # first store the next_curr which will be used later to update the curr node for
                # next iteration.
                next_curr = curr.next

                # if `prev` pointer is not None, update the next of it to the next of curr. Here,
                # we are removing the curr node from in-between.
                if prev is not None:
                    prev.next = curr.next

                # the curr node must now point to original head. Basically we have moved it just
                # before the head.
                curr.next = self.linked_list.head

                # However, we also need to update the tail pointer of the even part. So if, last_node
                # is not None, update the last_node's next to curr. Here is the structure right now.
                # dummy_node --> (some even nodes) --> last_node --> curr --> head --> ... tail --> None.
                if last_node is not None:
                    last_node.next = curr

                # also, if the curr node is the first even node that is being prepended, ensure to update
                # the dummy_node's next to this curr node. And this pointer will remain as is in future
                # iterations now. Basically, dummy_node.next is the first even node and will eventually
                # act as the updated head of the list.
                if dummy_node.next == self.linked_list.head:
                    dummy_node.next = curr

                # finally, move the last_node's next (tail of the even part) to last inserted even node, i.e.,
                # `curr` node. Also, update curr to `next_curr` which we stored. No need to update `prev` as
                # it will remain the same because we have moved a curr node and not moved forward in the traversal.
                last_node = curr
                curr = next_curr
            else:
                # however, if curr is either the head (irrespective if it's even or odd) or it is odd (irrespective
                # if it's head or not), move forward as you would normally do in a linked list traversal.
                prev = curr
                curr = curr.next

        # finally, the new head would be the dummy_node's next.
        self.linked_list.head = dummy_node.next

        # and the new tail would be prev, i.e., prev that is just before curr = None.
        self.linked_list.tail = prev


def test(_list):
    l = LinkedList()
    l.build(_list)
    l.show()
    splitter = LinkedListSplitter(l)
    splitter.split()
    l.show()
    print()


test([17, 15, 8, 9, 2, 4, 6])
test([1, 3, 5, 7])
test([17, 15, 8, 12, 10, 5, 4, 1, 7, 6])
test([1, 2, 3, 4, 5])
test([2, 1, 3, 5, 6, 4, 7])
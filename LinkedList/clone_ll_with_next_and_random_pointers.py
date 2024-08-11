class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.arb = None


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

    def get_index_of(self, node):
        if self.head is None:
            return None

        curr = self.head
        index = 0

        while curr is not None:
            if curr == node:
                return index
            curr = curr.next
            index += 1

        return None

    def get_node_at(self, index):
        if self.head is None:
            return

        if index < 0:
            return

        counter = 0
        curr = self.head
        while curr is not None:
            if counter == index:
                return curr
            curr = curr.next
            counter += 1

        return None

    def show(self):
        curr = self.head
        random_nodes = []

        while curr is not None:
            print(curr.data, end=" ")
            random_nodes.append((curr.data, curr.arb.data if curr.arb is not None else ''))
            curr = curr.next

        print()
        print(random_nodes)



def approach1():
    # In this approach, we first create all the new nodes using the original list, and
    # then create the linkages. This takes O(N) time and O(N) space.
    def clone_linked_list(linked_list):
        curr = linked_list.head

        # create a references dictionary which will store the copied version of each
        # node from the original linked list.
        references = dict()

        # start from the head node of the original linked list and create a copy of each
        # node and store their addresses in the references dictionary one by one. No linkages
        # to be done yet.
        while curr is not None:
            references[curr] = Node(curr.data)
            curr = curr.next

        # come back to the head node of the original list again.
        curr = linked_list.head

        # store a prev pointer. This will be useful when the new list will be returned because
        # at that time we would need reference to the tail pointer.
        prev = None

        # create the linkages in the copied list now
        while curr is not None:
            # get the copied node
            copied_node = references[curr]

            # assign the next and arbitrary pointers of the copied node using the curr
            # node from the `references` dictionary.
            copied_node.next = references[curr.next] if curr.next is not None else None
            copied_node.arb = references[curr.arb] if curr.arb is not None else None

            # update the prev variable by curr node
            prev = curr

            # move to next original node.
            curr = curr.next

        # create a new linked list, update its head and tail pointers and return it.
        copied_linked_list = LinkedList()
        copied_linked_list.head = references[linked_list.head]
        copied_linked_list.tail = prev
        return copied_linked_list

    # Example:
    l1 = LinkedList()
    for i in [7, 13, 11, 10, 1]:
        l1.push(i)

    # assign the pointers
    l1.head.next.arb = l1.head
    l1.head.next.next.arb = l1.tail
    l1.head.next.next.next.arb = l1.head.next.next
    l1.tail.arb = l1.head

    # clone the list and show
    l1_copied = clone_linked_list(l1)
    l1_copied.show()
    print(f"L1 is not equal to Copied L1: {l1.head != l1_copied.head}")

approach1()
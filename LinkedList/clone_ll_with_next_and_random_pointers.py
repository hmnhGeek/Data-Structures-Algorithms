# Problem link - https://www.geeksforgeeks.org/problems/clone-a-linked-list-with-next-and-random-pointer/1
# Solution - https://www.youtube.com/watch?v=q570bKdrnlw

# Approach 2 is something which I came up myself and solved it.

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


def approach2():
    # This approach takes O(N) time and O(1) space, although the iterations have increased
    # because of finding indices and nodes at those indices.
    def clone_linked_list(linked_list):
        curr = linked_list.head

        # create variables to store head and tail pointers of the copied list.
        # The `prev` pointer should be used to create linkages in the new list.
        # The prev pointer is not for storing tail information as was the case
        # in the approach 1.
        copied_head = None
        copied_tail = None
        prev = None

        while curr is not None:
            # create the new node
            new_node = Node(curr.data)

            # if the current node is original head, the new node must also be the head
            # of the copied list. Update the copied_head variable.
            if curr == linked_list.head:
                copied_head = new_node

            # if the current node is original tail, the new node must also be the tail
            # of the copied list. Update the copied_tail variable.
            if curr == linked_list.tail:
                copied_tail = new_node

            # The prev node is from the copied list that we are creating, and it is storing
            # the parent level information in the new list to create the next pointer linkages.
            if prev is not None:
                prev.next = new_node

            # move the prev pointer to new node as in the next iteration this will become
            # the parent of the next new node.
            prev = new_node

            # as usual, move the curr to next.
            curr = curr.next

        # create the new list and update its head and tail pointers
        copied_linked_list = LinkedList()
        copied_linked_list.head = copied_head
        copied_linked_list.tail = copied_tail

        # till now, in the new list we have only created the linkages of the next pointers.
        # We still have to create linkages of the arbitrary pointers.

        # both the lists will have same length
        orig_curr = linked_list.head
        new_curr = copied_head

        # iterate on original list
        while orig_curr is not None:
            # get the index of the arbitrary pointer of the original current node.
            index_of_orig_arb_pointer = linked_list.get_index_of(orig_curr.arb)

            # if the index is not None, then find the node at this index in the new list.
            # this will be the arbitrary node of the current node from the new list. if the
            # index was None, there is no need to do anything as `arb` pointers are by
            # default None only.
            if index_of_orig_arb_pointer is not None:
                new_arb_node = copied_linked_list.get_node_at(index_of_orig_arb_pointer)
                new_curr.arb = new_arb_node

            # move the current pointers to their respective next nodes at the same time.
            orig_curr = orig_curr.next
            new_curr = new_curr.next

        # once the arbitrary pointers are copied, we can return the copied list.
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


def approach3():
    # This approach takes O(N) time and O(1) space with no multiple O(N) iterations;
    # only 3 iterations are required unlike in approach 2, where to find the indices,
    # multiple iterations were required.
    def insert_new_nodes(linked_list: LinkedList):
        # This function creates a copy of every node in the list and assigns it as the
        # next pointer of the current node. The present next node of the current node
        # becomes the next node of the copied node. This happens in O(N) time.
        curr = linked_list.head
        while curr is not None:
            new_node = Node(curr.data)
            temp = curr.next
            curr.next = new_node
            new_node.next = temp
            curr = temp

    def update_arb_pointers(linked_list: LinkedList):
        # This function updates the arb pointers of the copied nodes (inserted in the original
        # list), by iterating in the modified original list. The idea is that the copied node
        # of each node from the original list lies as the next node. So if 7's arb pointer is
        # 13, then 7' (which is 7.next) arb pointer will be 13' (which is 13.next). This
        # operation happens in O(N) time.
        curr = linked_list.head
        while curr is not None:
            copied_node = curr.next
            copied_arb_node = curr.arb.next if curr.arb is not None else None
            if copied_node is not None:
                copied_node.arb = copied_arb_node
            curr = curr.next.next

    def extract_new_list(linked_list: LinkedList) -> LinkedList:
        # This function extracts the copied nodes that were inserted in the original list
        # and restores the original list back. So if the list is like 7 -> 7' -> 13 -> 13',
        # then 7.next = 7.next.next (13) and 7'.next = 13.next (i.e., 13'). This operation
        # takes O(N) time.
        head_of_new_list = linked_list.head.next
        tail_of_new_list = None
        curr = linked_list.head
        while curr is not None:
            next_node = curr.next.next
            copied_curr = curr.next
            curr.next = next_node
            copied_curr.next = next_node.next if next_node is not None else None
            curr = next_node
            if next_node is None:
                tail_of_new_list = copied_curr

        copied_list = LinkedList()
        copied_list.head = head_of_new_list
        copied_list.tail = tail_of_new_list
        return copied_list

    def clone_linked_list(linked_list: LinkedList) -> LinkedList:
        # We will divide this problem into 3 sub-problems.

        # The first sub-problem is to create new nodes and insert them in between the
        # original list only. For example: 7 -> 7' -> 13 -> 13' -> 11 -> 11' -> ...
        insert_new_nodes(linked_list)

        # Then we update the `arb` pointers of the copied nodes by iterating in the
        # modified list.
        update_arb_pointers(linked_list)

        # finally, once the arb pointers are assigned, we extract the copied node, restore
        # the original list and return the extracted list as new list.
        return extract_new_list(linked_list)

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


print(f"Approach 1: O(N) time and O(N) space")
approach1()
print()
print(f"Approach 2: O(N) time and O(1) space")
approach2()
print()
print(f"Approach 3: O(N) time and O(1) space")
approach3()
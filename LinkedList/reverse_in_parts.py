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
        prev = None
        curr = self.head

        while curr is not None:
            next_curr = curr.next
            curr.next = prev
            prev = curr
            curr = next_curr

        self.head, self.tail = self.tail, self.head

    def _get_kth_node(self, start_node, k):
        curr = start_node
        prev = None
        counter = 1
        while curr is not None:
            if counter == k:
                return curr
            prev = curr
            curr = curr.next
            counter += 1
        return prev

    def reverse_in_parts(self, num_parts):
        curr = self.head
        prev = None

        while curr is not None:
            kth_node = self._get_kth_node(curr, num_parts)
            next_curr = kth_node.next
            kth_node.next = None

            if prev is None:
                self.head = kth_node

            temp_linked_list = LinkedList()
            temp_linked_list.head = curr
            temp_linked_list.tail = kth_node
            temp_linked_list.reverse()

            if prev is not None:
                prev.next = kth_node

            prev = curr
            curr = next_curr

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
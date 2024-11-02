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
        if prev is None and node == self.head:
            self.head = self.head.next
            return

        if prev.next != node:
            return
        elif node == self.tail:
            prev.next = None
            self.tail = prev
        else:
            prev.next = node.next
        del node
        self.length -= 1

    def remove_duplicates(self):
        hash_map = {}
        second_occur = {}
        curr = self.head
        while curr is not None:
            second_occur[curr.data] = False
            if curr.data not in hash_map:
                hash_map[curr.data] = 1
            else:
                hash_map[curr.data] += 1
            curr = curr.next

        prev, curr = None, self.head
        while curr is not None:
            if hash_map[curr.data] > 1 and second_occur[curr.data]:
                temp = curr.next
                self.delete(prev, curr)
                hash_map[curr.data] -= 1
                curr = temp
            elif hash_map[curr.data] > 1 and not second_occur[curr.data]:
                second_occur[curr.data] = True
                prev = curr
                curr = curr.next
            else:
                prev = curr
                curr = curr.next

#
# l1 = LinkedList()
# l1.build(5, 2, 2, 4)
# l1.show()
# l1.remove_duplicates()
# l1.show()
#
# l2 = LinkedList()
# l2.build(2, 2, 2, 2, 2)
# l2.show()
# l2.remove_duplicates()
# l2.show()

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
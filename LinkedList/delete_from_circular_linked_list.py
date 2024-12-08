# Problem link - https://www.geeksforgeeks.org/deletion-circular-linked-list/


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
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
        self.tail.next = self.head
        self.length += 1

    def show(self):
        curr = self.head
        while curr.next != self.head:
            print(curr.data, end=" ")
            curr = curr.next
        print(curr.data, end=" ")
        print()

    def delete(self, index):
        """
            T: O(n) and S: O(1)
        """

        # if the list is empty or the index is out of bounds, return
        if self.is_empty():
            return
        if index not in range(self.length):
            return

        # store traversal variables.
        curr = self.head
        counter = 0
        prev = self.tail

        # while counter hasn't reached index
        while counter != index:
            # update prev and curr and increment the counter
            prev = curr
            curr = curr.next
            counter += 1

        # delete the linkage between prev and curr
        prev.next = curr.next

        # update head or tail if required.
        if curr == self.head:
            self.head = curr.next
        elif curr == self.tail:
            self.tail = prev

        # decrement the length
        self.length -= 1


cll = CircularLinkedList()
for i in [1, 2, 3, 4, 5, 6, 7, 8]:
    cll.push(i)
cll.show()
cll.delete(0)
cll.show()
cll.delete(5)
cll.show()
cll.delete(2)
cll.show()

# Problem link - https://www.geeksforgeeks.org/problems/add-1-to-a-number-represented-as-linked-list/1


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

    def build(self, _list):
        for i in _list:
            self.push(i)

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
            prev = curr
            curr = next_curr
        self.head, self.tail = self.tail, self.head

    def add_one(self):
        """
            Overall time complexity is O(n) and space complexity is O(1).
        """

        # define a carry variable
        carry = 0

        # reversing will take O(n) time.
        self.reverse()

        # iterate on the list in O(n) time.
        curr = self.head
        while curr is not None:
            # if in the reversed list, you are on the first node, you must explicitly add a 1.
            if curr == self.head:
                val = curr.data + carry + 1
            else:
                val = curr.data + carry

            # update carry and unit's place values
            carry = val // 10
            val = val % 10

            # update the node data with val value.
            curr.data = val

            # move to the next node
            curr = curr.next

        # after traversing, if there is a carry value, which would be a single digit only, then create a new node
        # for it and push it.
        if carry > 0:
            self.push(carry)

        # reverse the list again in O(n) time to get the final result.
        self.reverse()


def test(*args):
    l = LinkedList()
    l.build([i for i in args])
    l.show()
    l.add_one()
    l.show()
    print()


test(9, 9, 9)
test(4, 5, 6)
test(0, 0, 0)
test(1, 2, 3)
test(2, 1, 6, 9)
test(1, 5, 3)
test(9, 9)
test(0)
test(9)
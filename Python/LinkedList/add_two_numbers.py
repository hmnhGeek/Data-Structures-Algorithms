# Problem link - https://www.geeksforgeeks.org/problems/add-two-numbers-represented-by-linked-lists/1


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
            print(curr.data, end = " ")
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


class Solution:
    @staticmethod
    def add_nums(l1: LinkedList, l2: LinkedList) -> LinkedList:
        """
            Time complexity is O(n + m) and space complexity is O(max(n, m)), i.e., the longer list controls the length
            of the final list.
        """

        # create a result linked list.
        result = LinkedList()

        # reverse both the input lists to start adding from the unit's digit.
        # This will take O(n + m) time.
        l1.reverse()
        l2.reverse()

        # store a carry, and head pointers of both the input lists.
        carry = 0
        curr1, curr2 = l1.head, l2.head

        # All the while loops below will take O(n + m) time in total.

        # while both the linked lists have nodes to add...
        while curr1 is not None and curr2 is not None:
            # get the value by adding the node values and the carry value.
            val = curr1.data + curr2.data + carry

            # update the carry
            carry = val//10

            # push the value
            result.push(val % 10)

            # move to the next nodes in both the lists.
            curr1 = curr1.next
            curr2 = curr2.next

        # if l2 is exhausted but l1 still has nodes.
        while curr1 is not None:
            # get the value, update the carry and push to the result list.
            val = curr1.data + carry
            carry = val // 10
            result.push(val % 10)
            curr1 = curr1.next

        # or the other way round, l1 is exhausted but l2 has nodes.
        while curr2 is not None:
            val = curr2.data + carry
            carry = val // 10
            result.push(val % 10)
            curr2 = curr2.next

        # finally, if both the lists are exhausted, but the carry is not 0.
        while carry != 0:
            # push the carry % 10
            result.push(carry % 10)
            # update the carry.
            carry = carry // 10

        # restore the original lists. This will take another O(n + m) time.
        l1.reverse()
        l2.reverse()

        # reverse the result list and return the correct answer. This will take O(n + m) time.
        result.reverse()
        return result


def test(n1, n2):
    l1 = LinkedList()
    l1.build([int(i) for i in n1])
    l2 = LinkedList()
    l2.build([int(i) for i in n2])
    print("\nFirst linked list")
    l1.show()
    print("\nSecond linked list")
    l2.show()
    print("\nSummed linked list")
    summed = Solution.add_nums(l1, l2)
    summed.show()
    print("\n-------------Test completed------------\n")


test("545", "555")
test("45", "345")
test("0063", "07")
test("243", "564")
test("9"*7, "9"*4)
test("123", "999")

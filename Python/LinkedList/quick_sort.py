# Problem link - https://www.geeksforgeeks.org/problems/quick-sort-on-linked-list/1
# Solution - https://www.youtube.com/watch?v=ByUiqQGz5_w


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

    def build(self, *args):
        for i in args:
            self.push(i)

    def __str__(self):
        if self.is_empty():
            return "[]"
        result = "["
        curr = self.head
        while curr != self.tail:
            result += f"{curr.data}, "
            curr = curr.next
        result += f"{self.tail.data}]"
        return result


class Solution:
    @staticmethod
    def quick_sort(linked_list: LinkedList):
        """
            Time complexity is O(n^2) and space complexity is O(n).
        """

        # if the linked list is either empty or just has 1 element, then return the linked list as is.
        if linked_list.length == 0 or linked_list.length == 1:
            return linked_list

        # make the first element of the linked list, that is head of the linked list as pivot.
        pivot = linked_list.head

        # for iterating on the remaining list, initiate variable temp.
        temp = pivot.next

        # ensure that pivot is disconnected.
        pivot.next = None

        # tracking variables to store all smaller elements than pivot on the left.
        dummy_left = left = Node(None)
        left_length = 0

        # tracking variables to store all larger elements than pivot on the right.
        dummy_right = right = Node(None)
        right_length = 0

        # now iterate on the linked list
        while temp is not None:
            # keep track of next temp
            next_of_temp = temp.next

            # if the temp <= pivot, put temp on the left part
            if temp.data <= pivot.data:
                left.next = temp
                left = temp
                # ensure to break this link
                left.next = None
                # and update the left part's length
                left_length += 1
            else:
                # else put temp on the right part
                right.next = temp
                right = temp
                # ensure to break this link
                right.next = None
                # and update the right part's length
                right_length += 1

            # move to next temp
            temp = next_of_temp

        # create left and right linked lists for these segregated parts.
        left_linked_list = LinkedList()
        right_linked_list = LinkedList()

        # create the left linked list
        left_linked_list.length = left_length
        left_linked_list.head = dummy_left.next
        left_linked_list.tail = left

        # create the right linked list
        right_linked_list.length = right_length
        right_linked_list.head = dummy_right.next
        right_linked_list.tail = right

        # now, recursively sort these left and right linked lists before merging them with pivot.
        left_linked_list = Solution.quick_sort(left_linked_list)
        right_linked_list = Solution.quick_sort(right_linked_list)

        # if both left and right parts have some elements
        if not left_linked_list.is_empty() and not right_linked_list.is_empty():
            left_linked_list.tail.next = pivot
            pivot.next = right_linked_list.head
            linked_list.head = left_linked_list.head
            linked_list.tail = right_linked_list.tail
        elif not left_linked_list.is_empty():
            # if right part is empty...
            left_linked_list.tail.next = pivot
            linked_list.head = left_linked_list.head
            # then pivot becomes the tail of the sorted linked list
            linked_list.tail = pivot
        else:
            # if left part is empty...
            pivot.next = right_linked_list.head
            # then pivot becomes the head of the sorted linked list
            linked_list.head = pivot
            linked_list.tail = right_linked_list.tail

        # finally, return the sorted linked list
        return linked_list


def test(*args):
    l = LinkedList()
    l.build(*args)
    print(l)
    l = Solution.quick_sort(l)
    print(l)
    print()


test(1, 6, 2)
test(1, 9, 3, 8)
test(16, 3, 89, 2, 6, 4, 3)
test(10, 1, 10)
test(2, 18, 9, 45, 3, 68, 9, 24)

# Problem link - https://www.naukri.com/code360/problems/merge-sort-linked-list_920473
# Solution - https://www.youtube.com/watch?v=8ocB7a_c-Cc
# Solution for finding middle of linked list - https://www.youtube.com/watch?v=7LjQ57RqgEc


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

    def get_middle_node(self):
        if self.head is None:
            return
        slow = self.head
        fast = self.head.next
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow

    def show(self):
        curr = self.head
        while curr is not None:
            print(curr.data, end=" --> ")
            curr = curr.next
        print()

    def build(self, *args):
        for i in args:
            self.push(i)


class Solution:
    @staticmethod
    def _merge(left_linked_list, right_linked_list):
        # stand on the heads of both the linked lists
        curr1, curr2 = left_linked_list.head, right_linked_list.head

        # create a dummy and temp node both pointing to the same node for now.
        dummy_node = temp = Node(None)

        # iterate on both the sorted lists and merge the smaller nodes into dummy node.
        while curr1 is not None and curr2 is not None:
            if curr1.data <= curr2.data:
                temp.next = curr1
                temp = curr1
                curr1 = curr1.next
            else:
                temp.next = curr2
                temp = curr2
                curr2 = curr2.next
            temp.next = None

        # if there are elements left in first linked list, add them to dummy node.
        while curr1 is not None:
            temp.next = curr1
            temp = curr1
            curr1 = curr1.next
            temp.next = None

        # if there are elements left in second linked list, add them to dummy node.
        while curr2 is not None:
            temp.next = curr2
            temp = curr2
            curr2 = curr2.next
            temp.next = None

        # finally, create a merged linked list
        merged_linked_list = LinkedList()
        # point the head to dummy's next
        merged_linked_list.head = dummy_node.next
        # point the tail to temp node
        merged_linked_list.tail = temp
        # return the merged linked list
        return merged_linked_list

    @staticmethod
    def _merge_sort(linked_list: LinkedList):
        # if there is only a single node, return the linked list as is.
        if linked_list.head.next is None:
            return linked_list

        # get the mid of the linked list in O(n/2) time.
        mid = linked_list.get_middle_node()

        # break the linked list into two halves. `next_linked_list` now points to second half.
        next_linked_list = LinkedList()
        next_linked_list.head = mid.next
        next_linked_list.tail = linked_list.tail

        # ensure that you break the original linked list into first half.
        linked_list.tail = mid
        mid.next = None

        # divide and conquer on left and right lists.
        left_sorted_linked_list = Solution._merge_sort(linked_list)
        right_sorted_linked_list = Solution._merge_sort(next_linked_list)

        # get the sorted result by merging the left sorted and right sorted linked lists.
        return Solution._merge(left_sorted_linked_list, right_sorted_linked_list)

    @staticmethod
    def sort(linked_list: LinkedList):
        # get the sorted linked list. This will take O(n*log(n)) time and O(n) space.
        sorted_linked_list = Solution._merge_sort(linked_list)
        # update the head and tail of the original linked list so that they now point to the sorted linked list.
        linked_list.head = sorted_linked_list.head
        linked_list.tail = sorted_linked_list.tail


l = LinkedList()
l.build(3, 4, 2, 1, 5)
l.show()
Solution.sort(l)
l.show()

print()

l = LinkedList()
l.build(9, 15, 0)
l.show()
Solution.sort(l)
l.show()

print()

l = LinkedList()
l.build(40, 20, 60, 10, 50, 30)
l.show()
Solution.sort(l)
l.show()

print()

l = LinkedList()
l.build(9, 5, 2, 8)
l.show()
Solution.sort(l)
l.show()

print()

l = LinkedList()
l.build(1, -2, 3, -1)
l.show()
Solution.sort(l)
l.show()

print()

l = LinkedList()
l.build(9, 9, -1)
l.show()
Solution.sort(l)
l.show()
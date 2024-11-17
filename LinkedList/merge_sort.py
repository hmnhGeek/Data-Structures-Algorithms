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
        curr1, curr2 = left_linked_list.head, right_linked_list.head
        dummy_node = temp = Node(None)
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
        while curr1 is not None:
            temp.next = curr1
            temp = curr1
            curr1 = curr1.next
            temp.next = None
        while curr2 is not None:
            temp.next = curr2
            temp = curr2
            curr2 = curr2.next
            temp.next = None
        merged_linked_list = LinkedList()
        merged_linked_list.head = dummy_node.next
        merged_linked_list.tail = temp
        return merged_linked_list

    @staticmethod
    def _merge_sort(linked_list: LinkedList):
        if linked_list.head.next is None:
            return linked_list

        mid = linked_list.get_middle_node()
        next_linked_list = LinkedList()
        next_linked_list.head = mid.next
        next_linked_list.tail = linked_list.tail
        linked_list.tail = mid
        mid.next = None

        left_sorted_linked_list = Solution._merge_sort(linked_list)
        right_sorted_linked_list = Solution._merge_sort(next_linked_list)
        return Solution._merge(left_sorted_linked_list, right_sorted_linked_list)

    @staticmethod
    def sort(linked_list: LinkedList):
        sorted = Solution._merge_sort(linked_list)
        linked_list.head = sorted.head
        linked_list.tail = sorted.tail


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

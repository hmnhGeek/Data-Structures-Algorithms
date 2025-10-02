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
        if linked_list.length == 0 or linked_list.length == 1:
            return linked_list
        pivot = linked_list.head
        temp = pivot.next
        pivot.next = None
        dummy_left = left = Node(None)
        left_length = 0
        dummy_right = right = Node(None)
        right_length = 0
        while temp is not None:
            next_of_temp = temp.next
            if temp.data <= pivot.data:
                left.next = temp
                left = temp
                left.next = None
                left_length += 1
            else:
                right.next = temp
                right = temp
                right.next = None
                right_length += 1
            temp = next_of_temp
        left_linked_list = LinkedList()
        right_linked_list = LinkedList()

        left_linked_list.length = left_length
        left_linked_list.head = dummy_left.next
        left_linked_list.tail = left

        right_linked_list.length = right_length
        right_linked_list.head = dummy_right.next
        right_linked_list.tail = right

        left_linked_list = Solution.quick_sort(left_linked_list)
        right_linked_list = Solution.quick_sort(right_linked_list)

        if not left_linked_list.is_empty() and not right_linked_list.is_empty():
            left_linked_list.tail.next = pivot
            pivot.next = right_linked_list.head
            linked_list.head = left_linked_list.head
            linked_list.tail = right_linked_list.tail
        elif not left_linked_list.is_empty():
            left_linked_list.tail.next = pivot
            linked_list.head = left_linked_list.head
            linked_list.tail = pivot
        else:
            pivot.next = right_linked_list.head
            linked_list.head = pivot
            linked_list.tail = right_linked_list.tail
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

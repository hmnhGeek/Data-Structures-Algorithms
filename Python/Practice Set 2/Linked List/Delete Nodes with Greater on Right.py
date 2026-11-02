# Problem link - https://www.geeksforgeeks.org/problems/delete-nodes-having-greater-value-on-right/1


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
    def delete_right(linked_list: LinkedList):
        """
            Overall time complexity is O(n) and space complexity is O(1).
        """
        print(linked_list)
        linked_list.reverse()
        max_val = -1e6
        prev = None
        curr = linked_list.head
        while curr is not None:
            if max_val <= curr.data:
                max_val = curr.data
                prev = curr
                curr = curr.next
            else:
                next_curr = curr.next
                Solution._delete_node(linked_list, prev, curr)
                curr = next_curr

        linked_list.reverse()
        print(linked_list)
        print()

    @staticmethod
    def _delete_node(linked_list, prev, curr):
        if curr == linked_list.head:
            linked_list.head = linked_list.head.next
        elif curr == linked_list.tail:
            prev.next = None
            linked_list.tail = prev
        else:
            prev.next = curr.next
        linked_list.length -= 1

    @staticmethod
    def test(*args):
        linked_list = LinkedList()
        linked_list.build(*args)
        Solution.delete_right(linked_list)


Solution.test(12, 15, 10, 11, 5, 6, 2, 3)
Solution.test(10, 20, 30, 40, 50, 60)
Solution.test(5, 2, 13, 3, 8)
Solution.test(1, 1, 1, 1)

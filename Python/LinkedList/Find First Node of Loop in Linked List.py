# Problem link - https://www.geeksforgeeks.org/find-first-node-of-loop-in-a-linked-list/#expected-approach-using-floyds-loop-detection-algorithm-on-time-and-o1-space
# Solution - https://www.youtube.com/watch?v=2Kd0KKmmHFc

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

    def pop(self):
        if self.is_empty():
            return
        item = self.head.data
        node = self.head
        self.head = self.head.next
        del node
        return item

    def build(self, *args):
        for i in args:
            self.push(i)

    def __str__(self):
        if self.length == 0:
            return "[]"
        if self.length == 1:
            return f"[{self.head.data}]"
        result = f"[{self.head.data}, "
        curr = self.head.next
        while curr and curr != self.tail:
            result += f"{curr.data}, "
            curr = curr.next
        result += f"{self.tail.data}]"
        return result


class Solution:
    @staticmethod
    def find_first_node_of_loop(linked_list: LinkedList) -> Node | None:
        """
            Time complexity is O(n) and space complexity is O(n).
        """

        slow = fast = linked_list.head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = linked_list.head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None


# Example 1
l = LinkedList()
l.build(1, 3, 2, 4, 5)
print(l)
node1 = Solution.find_first_node_of_loop(l)
print(node1.data if node1 else None)
l.tail.next = l.head.next
node2 = Solution.find_first_node_of_loop(l)
print(node2.data if node2 else None)

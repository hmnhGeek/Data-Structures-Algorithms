# Problem link - https://www.geeksforgeeks.org/detect-loop-in-a-linked-list/#naive-approach-using-hashset-on-time-and-on-space


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


class LoopDetector:
    @staticmethod
    def floyd_loop_detection(linked_list: LinkedList) -> bool:
        """
            Time complexity is O(n) and space complexity is O(1).
        """

        # The idea is to store two pointers slow and fast. `slow` moves one node at a time
        # while `fast` moves two nodes at a time. At any point (except the start), if slow
        # and fast become the same, we have a loop.
        slow = fast = linked_list.head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    @staticmethod
    def memory_based_detection(linked_list: LinkedList) -> bool:
        """
            Time complexity is O(n) and space complexity is O(n).
        """

        # The idea is to store the nodes as you visit them into a set. If a node is found
        # in the set, there is a loop.
        visited = set()
        curr = linked_list.head
        while curr is not None:
            if curr in visited:
                return True
            visited.add(curr)
            curr = curr.next
        return False


linked_list1 = LinkedList()
for i in [1, 2, 3, 4, 5]:
    linked_list1.push(i)
linked_list1.tail.next = linked_list1.head.next.next.next
print(LoopDetector.floyd_loop_detection(linked_list1))
print(LoopDetector.memory_based_detection(linked_list1))

linked_list2 = LinkedList()
for i in [1, 2, 3, 4, 5]:
    linked_list2.push(i)
print(LoopDetector.floyd_loop_detection(linked_list2))
print(LoopDetector.memory_based_detection(linked_list2))
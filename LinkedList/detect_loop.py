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
        slow = fast = linked_list.head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


linked_list1 = LinkedList()
for i in [1, 2, 3, 4, 5]:
    linked_list1.push(i)
linked_list1.tail.next = linked_list1.head.next.next.next
print(LoopDetector.floyd_loop_detection(linked_list1))

linked_list2 = LinkedList()
for i in [1, 2, 3, 4, 5]:
    linked_list2.push(i)
print(LoopDetector.floyd_loop_detection(linked_list2))
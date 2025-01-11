class Node:
    def __init__(self, data):
        self.data = data
        self.next = self.random = None


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

    def show(self):
        curr = self.head
        while curr is not None:
            print(f"({curr.data}, {curr.random.data if curr.random else None})", end=" ")
            curr = curr.next
        print()


class Solution:
    @staticmethod
    def _insert_nodes(linked_list: LinkedList):
        curr = linked_list.head
        while curr is not None:
            temp = Node(curr.data)
            next_curr = curr.next
            curr.next = temp
            temp.next = next_curr
            curr = next_curr

    @staticmethod
    def _connect_random_pointers(linked_list: LinkedList):
        curr = linked_list.head
        while curr is not None:
            curr_copy = curr.next
            random_node = curr.random
            random_copy = random_node.next if random_node else None
            curr_copy.random = random_copy
            curr = curr_copy.next

    @staticmethod
    def _extract_cloned(linked_list: LinkedList):
        dummy_node = temp = Node(None)
        curr = linked_list.head
        while curr is not None:
            temp.next = curr.next
            next_temp = curr.next
            curr.next = next_temp.next
            temp = next_temp
            curr = curr.next
        return dummy_node.next, temp

    @staticmethod
    def clone(linked_list: LinkedList) -> LinkedList:
        Solution._insert_nodes(linked_list)
        Solution._connect_random_pointers(linked_list)
        head, tail = Solution._extract_cloned(linked_list)
        cloned_list = LinkedList()
        cloned_list.head = head
        cloned_list.tail = tail
        return cloned_list


# Example 1
l = LinkedList()
for i in [1, 2, 3, 4, 5]:
    l.push(i)
l.head.random = l.head.next.next
l.head.next.random = l.head
l.head.next.next.next.random = l.head.next.next
l.tail.random = l.head.next
l.show()
cloned = Solution.clone(l)
cloned.show()
print()

# Example 2
l = LinkedList()
for i in [7, 13, 11, 10, 1]:
    l.push(i)
l.head.next.random = l.head
l.head.next.next.random = l.tail
l.head.next.next.next.random = l.head.next.next
l.tail.random = l.head
l.show()
cloned = Solution.clone(l)
cloned.show()

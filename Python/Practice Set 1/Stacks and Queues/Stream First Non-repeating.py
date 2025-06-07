# Problem link - https://www.geeksforgeeks.org/problems/first-non-repeating-character-in-a-stream1216/1


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = self.next = None


class DoublyLinkedList:
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
            node.prev = self.tail
            self.tail = node
        self.length += 1
        return node

    def front(self):
        if self.is_empty():
            return "#"
        return self.head.data

    def remove(self, node: Node):
        is_tail, is_head = node == self.tail, node == self.head
        prev = node.prev
        next_node = node.next
        if prev:
            prev.next = next_node
        if next_node:
            next_node.prev = prev
        del node
        self.length -= 1
        if is_head:
            self.head = next_node
        if is_tail:
            self.tail = prev


class Solution:
    @staticmethod
    def get_dict(default):
        alphabets = "abcdefghijklmnopqrstuvwxyz"
        d = {}
        for i in alphabets:
            d[i] = default
        return d

    @staticmethod
    def find_first_non_repeating(string):
        """
            Time complexity is O(n) and space complexity is O(1).
        """

        # these will take O(1) space.
        address = Solution.get_dict(None)
        repeated = Solution.get_dict(False)
        dll = DoublyLinkedList()
        result = ""

        # loop in the string in O(n)
        for i in string:
            if repeated[i]:
                continue
            elif address[i] is not None:
                repeated[i] = True
                dll.remove(address[i])
            else:
                node = dll.push(i)
                address[i] = node
            result += dll.front()
        return result


print(Solution.find_first_non_repeating("aabc"))
print(Solution.find_first_non_repeating("zz"))
print(Solution.find_first_non_repeating("bb"))
print(Solution.find_first_non_repeating("abcbbac"))

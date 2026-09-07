# Problem link - https://www.geeksforgeeks.org/problems/check-mirror-in-n-ary-tree1528/1
# Solution - https://www.youtube.com/watch?v=oH63SpSshm0


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
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
            node.next = self.head
            self.head = node
        self.length += 1

    def pop(self):
        if self.is_empty():
            return
        item = self.head.data
        self.head = self.head.next
        self.length -= 1
        return item


class Solution:
    @staticmethod
    def check_mirror(arr, mirror):
        """
            Time complexity is O(e) and space complexity is O(e).
        """
        mp = {}
        for i in arr:
            mp[i] = Stack()
        n = len(arr)
        for i in range(0, n, 2):
            mp[arr[i]].push(arr[i + 1])
        for i in range(0, n, 2):
            if mirror[i + 1] != mp[arr[i]].pop():
                return False
        return True


print(Solution.check_mirror([1, 2, 1, 3], [1, 3, 1, 2]))
print(Solution.check_mirror([1, 2, 1, 3], [1, 2, 1, 3]))

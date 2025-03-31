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
        node = self.head
        self.head = self.head.next
        del node
        self.length -= 1
        return item

    def top(self):
        if self.is_empty():
            return
        return self.head.data


class Solution:
    @staticmethod
    def check_mirror(t1, t2):
        """
            Time complexity is O(n) and space complexity is O(e).
        """

        # create a dictionary storing the stacks for each even index.
        d = {i: Stack() for i in t1}
        n = len(t1)

        # push the edges from even indexed source node to odd indexed destination node. This will take O(n) time
        # and O(e) space.
        for i in range(0, n, 2):
            d[t1[i]].push(t1[i + 1])

        # now loop in the mirror array in O(n) time and since stack stores reverse order for each level, check for
        # mirror in each level.
        for i in range(0, n, 2):
            s = d[t2[i]]
            if s.top() == t2[i + 1]:
                s.pop()
            else:
                return False
        return True


print(Solution.check_mirror([1, 2, 1, 3], [1, 3, 1, 2]))
print(Solution.check_mirror([1, 2, 1, 3], [1, 2, 1, 3]))
print(Solution.check_mirror([1, 2, 1, 3, 1, 4, 4, 5, 4, 6, 6, 7, 7, 8, 7, 9, 7, 10, 7, 11], [1, 4, 1, 3, 1, 2, 4, 6, 4, 5, 6, 7, 7, 11, 7, 10, 7, 9, 7, 8]))
print(Solution.check_mirror([1, 2, 1, 3, 1, 4, 3, 5, 3, 6, 3, 7], [1, 4, 1, 3, 1, 2, 3, 6, 3, 5, 3, 7]))

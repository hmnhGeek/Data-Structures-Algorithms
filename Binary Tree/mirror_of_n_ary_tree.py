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
        d = {i: Stack() for i in t1}
        n = len(t1)
        for i in range(0, n, 2):
            d[t1[i]].push(t1[i + 1])
        for i in range(0, n, 2):
            s = d[t2[i]]
            if s.top() == t2[i + 1]:
                s.pop()
            else:
                return False
        return True


print(Solution.check_mirror([1, 2, 1, 3], [1, 3, 1, 2]))
print(Solution.check_mirror([1, 2, 1, 3], [1, 2, 1, 3]))

# Problem link - https://www.geeksforgeeks.org/interleave-first-half-queue-second-half/


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
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
        self.length -= 1
        return item

    def get_mid(self):
        slow = fast = self.head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def __str__(self):
        curr = self.head
        result = ""
        while curr is not None:
            result += f"{curr.data} "
            curr = curr.next
        return result


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

    def __str__(self):
        curr = self.head
        result = ""
        while curr is not None:
            result += f"{curr.data} "
            curr = curr.next
        return result


class Solution:
    @staticmethod
    def interleave(q: Queue):
        """
            Time complexity is O(n) and space complexity is O(n).
        """

        stack = Stack()

        # get the mid of the queue in O(n) time.
        mid = q.get_mid()

        # push the mid-node in stack
        stack.push(mid)

        # now start traversing the half of the queue in O(n) time.
        curr = q.head
        while curr != mid:
            # pop node from stack and push curr in between
            node = stack.pop()
            stack.push(curr)
            stack.push(node)
            if node.next is not None:
                stack.push(node.next)
            curr = curr.next

        # populate the queue in correct order in O(n) time.
        while not q.is_empty():
            q.pop()
        while not stack.is_empty():
            q.push(stack.pop().data)
        while not q.is_empty():
            stack.push(q.pop())
        while not stack.is_empty():
            q.push(stack.pop())


q = Queue()
for i in [1, 2, 3, 4]:
    q.push(i)
print(q)
Solution.interleave(q)
print(q)

q = Queue()
q.push(11)
q.push(12)
q.push(13)
q.push(14)
q.push(15)
q.push(16)
q.push(17)
q.push(18)
q.push(19)
q.push(20)
print(q)
Solution.interleave(q)
print(q)

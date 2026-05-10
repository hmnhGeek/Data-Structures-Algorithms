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

    def __str__(self):
        if self.is_empty():
            return "[]"
        curr = self.head
        result = "["
        while curr != self.tail:
            result += f"{curr.data}, "
            curr = curr.next
        result += f"{self.tail.data}]"
        return result


class Solution:
    @staticmethod
    def sort(stack: Stack):
        return Solution._sort(stack)

    @staticmethod
    def _sort(stack: Stack):
        if stack.head is None or stack.head.next is None:
            return stack
        middle_node = Solution._get_middle_node(stack)
        second_head = middle_node.next
        middle_node.next = None
        first = Stack()
        first.head = stack.head
        first.tail = middle_node
        first.length = stack.length // 2 if stack.length % 2 == 0 else stack.length // 2 + 1
        second = Stack()
        second.head = second_head
        second.tail = stack.tail
        second.length = stack.length // 2
        first = Solution._sort(first)
        second = Solution._sort(second)
        return Solution._merge(first, second)

    @staticmethod
    def _get_middle_node(stack: Stack) -> Node:
        slow, fast = stack.head, stack.head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    @staticmethod
    def _merge(first: Stack, second: Stack) -> Stack:
        dummy_node = Node(None)
        temp = dummy_node
        i, j = first.head, second.head
        while i is not None and j is not None:
            if i.data <= j.data:
                temp.next = i
                i = i.next
            else:
                temp.next = j
                j = j.next
            temp = temp.next
        while i is not None:
            temp.next = i
            i = i.next
            temp = temp.next
        while j is not None:
            temp.next = j
            j = j.next
            temp = temp.next
        result = Stack()
        result.head = dummy_node.next
        result.tail = temp
        result.length = first.length + second.length
        return result


def test(*args):
    global i
    stack = Stack()
    for i in args:
        stack.push(i)
    print(stack)
    stack = Solution.sort(stack)
    print(stack)
    print()


test(41, 3, 32, 2, 11)
test(3, 2, 1)
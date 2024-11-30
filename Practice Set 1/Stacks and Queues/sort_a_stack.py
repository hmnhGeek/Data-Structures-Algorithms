# Problem link - https://www.geeksforgeeks.org/sort-a-stack-using-recursion/


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
            return -1e6
        return self.head.data


class Solution:
    @staticmethod
    def _sorted_insert(stack, top, element):
        # if the element to insert is None, simply return the stack, you've sorted the stack.
        if element is None:
            return stack

        # if top element is less than current element, push the current element first and then
        # push the prev element from the recursion stack.
        if stack.top() <= element:
            stack.push(element)
            if top:
                stack.push(top)
            return stack

        # gte the sorted stack
        stack = Solution._sorted_insert(stack, stack.pop(), element)
        # if there is some previous element, push it back.
        if top:
            stack.push(top)
        # finally return the stack.
        return stack

    @staticmethod
    def _sort(stack: Stack, element):
        # if the stack is empty, simply insert the element and return stack. This will happen when the recursion for
        # `_sort` ends.
        if stack.is_empty():
            stack.push(element)
            return stack

        # else, if stack is not yet empty, pop an element and _sort recursively.
        stack = Solution._sort(stack, stack.pop())
        # start building back the stack backwards, by inserting elements in sorted fashion.
        stack = Solution._sorted_insert(stack, None, element)
        return stack

    @staticmethod
    def sort_stack(stack: Stack):
        # start with no element and begin the sorting process.
        Solution._sort(stack, None)
        while not stack.is_empty():
            print(stack.pop(), end=" ")
        print()


def test(*args):
    stack = Stack()
    for i in args:
        stack.push(i)
    Solution.sort_stack(stack)


test(11, 2, 32, 3, 41)
test(-3, 14, 18, -5, 30)
test(1, 2, 3)
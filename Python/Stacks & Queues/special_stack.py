# Problem link - https://www.geeksforgeeks.org/problems/special-stack/1


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self, capacity):
        self.head = self.tail = None
        self.length = 0
        self.capacity = capacity

    def is_empty(self):
        return self.length == 0

    def is_full(self):
        return self.length == self.capacity

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


class SpecialStack:
    def __init__(self, capacity):
        self.main_stack = Stack(capacity)
        self.temp_stack = Stack(capacity)

    def is_empty(self):
        return self.main_stack.is_empty()

    def is_full(self):
        return self.main_stack.is_full()

    def push(self, x):
        self.main_stack.push(x)

    def pop(self):
        return self.main_stack.pop()

    def get_min(self):
        """
            Time complexity is O(n) and space complexity is O(1).
        """
        # min value
        min_val = 1e6

        # O(n)
        while not self.main_stack.is_empty():
            popped = self.main_stack.pop()
            min_val = min(min_val, popped)
            self.temp_stack.push(min_val)

        # O(n)
        while not self.temp_stack.is_empty():
            self.main_stack.push(self.temp_stack.pop())
        return min_val


stack = SpecialStack(5)
for i in [18, 19, 29, 15, 16]:
    print(stack.get_min(), end=" ")
    print()
    stack.push(i)
    print(stack.is_full())

print()
print()

stack1 = SpecialStack(4)
for i in [34, 335, 1814, 86]:
    print(stack1.get_min(), end=" ")
    print()
    stack1.push(i)
    print(stack1.is_full())

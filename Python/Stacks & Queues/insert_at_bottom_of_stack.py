# Problem link - https://www.naukri.com/code360/problems/insert-an-element-at-its-bottom-in-a-given-stack_1171166


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

    def push_back(self, x):
        # if the stack is empty, simply push x into stack in O(1) time.
        if self.is_empty():
            self.push(x)
        else:
            # else push the node for x after the tail of the stack in O(1) time.
            node = Node(x)
            self.tail.next = node
            self.tail = node
            self.length += 1


stack = Stack()
for i in [7, 1, 4, 5]:
    stack.push(i)

stack.push_back(9)
while not stack.is_empty():
    print(stack.pop())

# Problem link - https://www.geeksforgeeks.org/problems/implement-two-stacks-in-an-array/1


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

    def push_back(self, x):
        node = Node(x)
        if self.is_empty():
            self.head = self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.length += 1

    def push_front(self, x):
        node = Node(x)
        if self.is_empty():
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.length += 1

    def pop_back(self):
        if self.is_empty():
            return
        item = self.tail.data
        node = self.tail
        self.tail = self.tail.prev
        self.tail.next = None
        del node
        self.length -= 1
        return item

    def pop_front(self):
        if self.is_empty():
            return
        item = self.head.data
        node = self.head
        self.head = self.head.next
        self.head.prev = None
        del node
        self.length -= 1
        return item


class TwoStacks:
    def __init__(self):
        self.stack = DoublyLinkedList()
        self.l1 = 0
        self.l2 = 0

    def push1(self, x):
        self.stack.push_front(x)
        self.l1 += 1

    def push2(self, x):
        self.stack.push_back(x)
        self.l2 += 1

    def pop1(self):
        if self.l1 != 0:
            self.l1 -= 1
            return self.stack.pop_front()

    def pop2(self):
        if self.l2 != 0:
            self.l2 -= 1
            return self.stack.pop_back()


stacks = TwoStacks()
stacks.push1(2)
stacks.push1(3)
stacks.push2(4)
print(stacks.pop1())
print(stacks.pop2())
print(stacks.pop2())

stacks2 = TwoStacks()
stacks2.push1(1)
stacks2.push2(2)
print(stacks2.pop1())
stacks2.push1(3)
print(stacks2.pop1())
print(stacks2.pop1())

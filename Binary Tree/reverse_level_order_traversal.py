# Problem link - https://www.geeksforgeeks.org/problems/reverse-level-order-traversal/1


from abc import ABC, abstractmethod


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class DataNode:
    def __init__(self, data, level):
        self.data = data
        self.level = level


class Node:
    def __init__(self, node: DataNode):
        self.data = node
        self.next = None


class CollectionInterface(ABC):
    def __init__(self):
        self.head = self.tail = None
        self.length = 0

    @abstractmethod
    def push(self, node: DataNode):
        pass

    @abstractmethod
    def pop(self):
        pass

    def is_empty(self):
        return self.length == 0


class Stack(CollectionInterface):
    def pop(self):
        if self.is_empty():
            return
        item = self.head.data
        node = self.head
        self.head = self.head.next
        del node
        self.length -= 1
        return item

    def push(self, x: DataNode):
        node = Node(x)
        if self.is_empty():
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head = node
        self.length += 1


class Queue:
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def push(self, x: DataNode):
        while not self.s1.is_empty():
            self.s2.push(self.s1.pop())
        self.s1.push(x)
        while not self.s2.is_empty():
            self.s1.push(self.s2.pop())

    def pop(self):
        return self.s1.pop()

    def is_empty(self):
        return self.s1.is_empty()


class Solution:
    @staticmethod
    def reverse_level_order(root: TreeNode):
        # create blank stack and queue data structures
        stack = Stack()
        queue = Queue()

        # push the root node with level 0.
        queue.push(DataNode(root, 0))

        # do the BFS traversal till the queue is not empty.
        while not queue.is_empty():
            # pop the current data node from queue.
            node = queue.pop()
            # push the data node to the stack.
            stack.push(node)

            # now first check the right child instead of left and push it to the queue with +1 level value.
            # We check right first because in the reversed order we want to see left child first when popping out from
            # the stack.
            if node.data.right is not None:
                queue.push(DataNode(node.data.right, node.level + 1))
            if node.data.left is not None:
                queue.push(DataNode(node.data.left, node.level + 1))

        # once stack is populated, pop from it until it becomes empty and store the integer data in the result list.
        result = []
        while not stack.is_empty():
            result.append(stack.pop().data.data)

        # the result list finally contains the reversed level order traversal.
        return result


# Example 1
one, two, three = TreeNode(1), TreeNode(2), TreeNode(3)
one.left = two
one.right = three
print(Solution.reverse_level_order(one))

# Example 2
ten, twenty, thirty, fourty, sixty = TreeNode(10), TreeNode(20), TreeNode(30), TreeNode(40), TreeNode(60)
ten.left = twenty
twenty.left = fourty
ten.right = thirty
twenty.right = sixty
print(Solution.reverse_level_order(ten))
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = self.tail = None
        self.length = 0

    def push(self, x):
        node = Node(x)
        if self.is_empty():
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.length += 1

    def is_empty(self):
        return self.length == 0

    def pop(self):
        if self.is_empty():
            return
        item = self.head.data
        node = self.head
        self.head = self.head.next
        del node
        self.length -= 1
        return item


class Utility:
    @staticmethod
    def is_complete_tree(root: TreeNode):
        queue = Queue()
        queue.push(root)
        found_null = False
        while not queue.is_empty():
            node = queue.pop()
            if node is None:
                found_null = True
            else:
                if found_null:
                    return False
                queue.push(node.left)
                queue.push(node.right)
        return True


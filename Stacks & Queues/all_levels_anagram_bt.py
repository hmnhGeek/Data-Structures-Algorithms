class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class QueueNode:
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
        node = QueueNode(x)

        if self.is_empty():
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node

        self.length += 1

    def pop(self):
        if self.is_empty():
            return

        item, node = self.head.data, self.head
        self.head = self.head.next
        del node
        self.length -= 1
        return item


class BinaryTree:
    def __init__(self, root):
        self.root = root

    def get_level_order(self):
        queue = Queue()
        if self.root is not None:
            queue.push((self.root, 0))
        level_order_traversal = {}

        while not queue.is_empty():
            node, level = queue.pop()
            if level not in level_order_traversal:
                level_order_traversal[level] = [node.data]
            else:
                level_order_traversal[level].append(node.data)

            if node.left is not None:
                queue.push((node.left, level + 1))
            if node.right is not None:
                queue.push((node.right, level + 1))
        return level_order_traversal


# Example 1
one, two, three, four, five = TreeNode(1), TreeNode(2), TreeNode(3), TreeNode(4), TreeNode(5)
one.left = three
two.left = five
one.right = two
two.right = four
tree = BinaryTree(one)
print(tree.get_level_order())
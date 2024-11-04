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


class TreeNode:
    def __init__(self, data):
        self.left = self.right = None
        self.data = data


class LeftView:
    @staticmethod
    def _solve(root: TreeNode, level: int, queue: Queue):
        if root is None:
            return

        if queue.length == level:
            queue.push(root.data)

        LeftView._solve(root.left, level + 1, queue)
        LeftView._solve(root.right, level + 1, queue)

    @staticmethod
    def get_recursive_view(root: TreeNode):
        queue = Queue()
        LeftView._solve(root, 0, queue)
        while not queue.is_empty():
            print(queue.pop(), end=" ")
        print()


# Example 1
n1, n2, n3, n4, n5, n6, n7 = TreeNode(1), TreeNode(2), TreeNode(3), TreeNode(4), TreeNode(5), TreeNode(6), TreeNode(7)
n1.left = n2
n2.left = n4
n5.left = n6
n1.right = n3
n3.right = n7
n2.right = n5
LeftView.get_recursive_view(n1)

# Example 2
n1, n2, n3, n4, n5, n6, n7, n8 = TreeNode(1), TreeNode(2), TreeNode(3), TreeNode(4), TreeNode(5), TreeNode(6), TreeNode(7), TreeNode(8)
n1.left = n2
n2.left = n4
n4.right = n8
n2.right = n5
n1.right = n3
n3.left = n6
n3.right = n7
LeftView.get_recursive_view(n1)
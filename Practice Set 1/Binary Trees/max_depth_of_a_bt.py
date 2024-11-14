class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class BinaryTree:
    def __init__(self, root: Node):
        self.root = root
        self._max_depth = 0

    def _get_max_depth(self, start: Node, level: int):
        if start is None:
            return
        self._max_depth = max(self._max_depth, level)
        self._get_max_depth(start.left, level + 1)
        self._get_max_depth(start.right, level + 1)

    def get_max_depth(self):
        self._max_depth = 0
        self._get_max_depth(self.root, 1)
        return self._max_depth


class MainSolution:
    def __init__(self, root: Node):
        self.root = root

    def get_depth(self, root: Node):
        if root is None:
            return 0
        left_ht = self.get_depth(root.left)
        right_ht = self.get_depth(root.right)
        return 1 + max(left_ht, right_ht)


# Example 1
n1, n2, n3, n4, n5, n6 = Node(1), Node(2), Node(3), Node(4), Node(5), Node(6)
n1.left = n2
n1.right = n3
n3.left = n4
n4.left = n5
n3.right = n6
t = BinaryTree(n1)
print(t.get_max_depth())
t1 = MainSolution(n1)
print(t1.get_depth(n1))
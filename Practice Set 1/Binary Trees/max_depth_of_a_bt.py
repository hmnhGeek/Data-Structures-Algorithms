# Video - https://www.youtube.com/watch?v=eD3tmO66aBA&list=PLgUwDviBIf0q8Hkd7bK2Bpryj2xVJk8Vk&index=15


class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class BinaryTree:
    def __init__(self, root: Node):
        self.root = root
        self._max_depth = 1

    def _get_max_depth(self, start: Node, level: int):
        # if a null node is encountered, return from the recursion
        if start is None:
            return
        # update the height by taking max of current level and previous max height encountered.
        self._max_depth = max(self._max_depth, level)

        # recursively increase level count for left and right subtree.
        self._get_max_depth(start.left, level + 1)
        self._get_max_depth(start.right, level + 1)

    def get_max_depth(self):
        """
            Time complexity is O(n) and space complexity is O(n).
        """

        # set global max height to 1 for root node.
        self._max_depth = 1
        # start with root node with level 1 or ht = 1.
        self._get_max_depth(self.root, 1)
        # return the height.
        return self._max_depth


class MainSolution:
    def __init__(self, root: Node):
        self.root = root

    def get_depth(self, root: Node):
        """
            Time complexity is O(n) and space complexity is O(n).
        """

        # root is null? return 0 height.
        if root is None:
            return 0

        # obtain left and right heights
        left_ht = self.get_depth(root.left)
        right_ht = self.get_depth(root.right)

        # return the height at root node.
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
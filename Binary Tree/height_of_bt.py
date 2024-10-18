class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


class BinaryTree:
    @staticmethod
    def _get_height(root: Node, depth: int) -> int:
        if root is None:
            return 0

        if root.left is None and root.right is None:
            return depth

        left = -1e6
        if root.left:
            left = BinaryTree._get_height(root.left, depth + 1)

        right = -1e6
        if root.right:
            right = BinaryTree._get_height(root.right, depth + 1)

        return max(left, right)

    @staticmethod
    def get_height(root: Node) -> int:
        return BinaryTree._get_height(root, 1)


# Example 1
one, two, three = Node(1), Node(2), Node(3)
one.left = two
one.right = three
print(BinaryTree.get_height(one))

# Example 2
one, two, three = Node(1), Node(2), Node(3)
two.right = one
one.left = three
print(BinaryTree.get_height(two))

# Example 3
n12, n8, n18, n5, n11 = Node(12), Node(8), Node(18), Node(5), Node(11)
n12.left = n8
n8.left = n5
n12.right = n18
n8.right = n11
print(BinaryTree.get_height(n12))
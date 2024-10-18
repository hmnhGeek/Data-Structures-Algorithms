# Problem link - https://www.geeksforgeeks.org/problems/height-of-binary-tree/1


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


class BinaryTree:
    @staticmethod
    def _get_height(root: Node, depth: int) -> int:
        # if the node is itself is None, return a 0 height
        if root is None:
            return 0

        # if the root node is a leaf node, return the current depth.
        if root.left is None and root.right is None:
            return depth

        # assume the left height to be -inf for the left subtree of the current root.
        left = -1e6
        if root.left:
            # if there exist a left subtree, get its height by passing `depth + 1` as height for the left node.
            left = BinaryTree._get_height(root.left, depth + 1)

        # assume the right height to be -inf for the right subtree of the current root.
        right = -1e6
        if root.right:
            # if there exist a right subtree, get its height by passing `depth + 1` as height for the right node.
            right = BinaryTree._get_height(root.right, depth + 1)

        # return the max height achieved from both the subtrees of the root.
        return max(left, right)

    @staticmethod
    def get_height(root: Node) -> int:
        """
            Time complexity would be O(n) and space complexity would be O(height) for the stack space.
        """

        # start from the root node with a height of 1.
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

# Example 4
n1, n2, n3, n4, n5, n6, n7 = Node(1), Node(2), Node(3), Node(4), Node(5), Node(6), Node(7)
n1.left = n2
n2.left = n4
n5.left = n6
n1.right = n3
n3.right = n5
n5.right = n7
print(BinaryTree.get_height(n1))

# Example 5
n1, n2, n5, n4, n6, n55 = Node(1), Node(2), Node(5), Node(4), Node(6), Node(5)
n1.left = n2
n5.left = n4
n4.left = n55
n1.right = n5
n5.right = n6
print(BinaryTree.get_height(n1))
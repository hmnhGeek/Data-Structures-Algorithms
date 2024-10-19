class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class BinaryTree:
    @staticmethod
    def _get_height(root: Node) -> int:
        if root is None:
            return 0
        return 1 + max(BinaryTree._get_height(root.left), BinaryTree._get_height(root.right))

    @staticmethod
    def get_diameter(root: Node) -> int:
        return 1 + BinaryTree._get_height(root.left) + BinaryTree._get_height(root.right)


# Example 1
ten, twenty, thirty, fourty, fifty, sixty = Node(10), Node(20), Node(30), Node(40), Node(50), Node(60)
ten.left = twenty
twenty.left = fourty
fourty.left = fifty
ten.right = thirty
twenty.right = sixty
print(BinaryTree.get_diameter(ten))

# Example 2
one, two, three = Node(1), Node(2), Node(3)
one.left = two
one.right = three
print(BinaryTree.get_diameter(one))
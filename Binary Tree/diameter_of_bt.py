class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class BinaryTree:
    @staticmethod
    def _get_height(root: Node, maxi: int):
        if root is None:
            return 0, maxi
        left_height, maxi = BinaryTree._get_height(root.left, maxi)
        right_height, maxi = BinaryTree._get_height(root.right, maxi)
        maxi = max(maxi, 1 + left_height + right_height)
        return 1 + max(left_height, right_height), maxi

    @staticmethod
    def get_diameter(root: Node) -> int:
        _, diameter = BinaryTree._get_height(root, 0)
        return diameter



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

# Example 3
n1, n2, n3, n4, n5, n6, n7, n8, n9 = Node(1), Node(2), Node(3), Node(4), Node(5), Node(6), Node(7), Node(8), Node(9)
n1.left = n2
n3.left = n4
n4.left = n5
n5.left = n6
n1.right = n3
n3.right = n7
n7.right = n8
n8.right = n9
print(BinaryTree.get_diameter(n1))
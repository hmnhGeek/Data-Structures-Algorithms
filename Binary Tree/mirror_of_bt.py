class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class TreeInorder:
    @staticmethod
    def get(root: Node):
        if root:
            TreeInorder.get(root.left)
            print(root.data, end=" ")
            TreeInorder.get(root.right)


class Solution:
    @staticmethod
    def _get_mirror(root: Node):
        if root is None:
            return

        left_subtree_root = root.left
        root.left = root.right
        root.right = left_subtree_root
        Solution._get_mirror(root.left)
        Solution._get_mirror(root.right)

    @staticmethod
    def get_mirror(root: Node):
        print()
        Solution._get_mirror(root)
        TreeInorder.get(root)


# Example 1
two, three, four, five, six = Node(2), Node(3), Node(4), Node(5), Node(6)
five.left = three
three.left = two
five.right = six
three.right = four
TreeInorder.get(five)
Solution.get_mirror(five)

print()
print()
# Example 2
one, two, eight, nine, twelve = Node(1), Node(2), Node(8), Node(9), Node(12)
two.left = one
one.left = twelve
two.right = eight
eight.right = nine
TreeInorder.get(two)
Solution.get_mirror(two)
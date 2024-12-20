# Problem link - https://www.geeksforgeeks.org/create-a-mirror-tree-from-the-given-binary-tree/


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
    """
        Overall time complexity is O(n) and space complexity is O(n).
    """

    @staticmethod
    def _get_mirror(root: Node):
        # if the node you're asking for does not exist, simply end the recursion.
        if root is None:
            return

        # store the reference to the left node of the root.
        left_subtree_root = root.left

        # LATERAL INVERSION
        # update the left node of the root to its right node
        root.left = root.right
        # update the right node of the root to the stored left node.
        root.right = left_subtree_root

        # recursively call this mirror method on left and right subtrees of the root.
        Solution._get_mirror(root.left)
        Solution._get_mirror(root.right)

    @staticmethod
    def get_mirror(root: Node):
        """Modifies the existing tree"""
        print()
        Solution._get_mirror(root)
        TreeInorder.get(root)

    @staticmethod
    def _get_new_mirror_tree(root: Node, root_dash: Node):
        # if either of the nodes is None, end the recursion.
        if root is None or root_dash is None:
            return

        # Lateral Inversion
        root_dash.left = Node(root.right.data) if root.right else None
        root_dash.right = Node(root.left.data) if root.left else None

        # recursively call for the left and right subtrees of the new tree.
        Solution._get_new_mirror_tree(root.right, root_dash.left)
        Solution._get_new_mirror_tree(root.left, root_dash.right)

    @staticmethod
    def get_mirror_tree(root: Node):
        """Creates a new tree in O(n) time and O(n) space."""
        print()
        if root is None:
            return
        mirror_root = Node(root.data)
        Solution._get_new_mirror_tree(root, mirror_root)
        return mirror_root


# Example 1
two, three, four, five, six = Node(2), Node(3), Node(4), Node(5), Node(6)
five.left = three
three.left = two
five.right = six
three.right = four
TreeInorder.get(five)
mirror = Solution.get_mirror_tree(five)
TreeInorder.get(mirror)

print()
print()
# Example 2
one, two, eight, nine, twelve = Node(1), Node(2), Node(8), Node(9), Node(12)
two.left = one
one.left = twelve
two.right = eight
eight.right = nine
TreeInorder.get(two)
mirror = Solution.get_mirror_tree(two)
TreeInorder.get(mirror)

print()
print()
# Example 3
five, three, six, two, four, eight, ten, eleven, twelve, thirteen = Node(5), Node(3), Node(6), Node(2), Node(4), Node(8), Node(10), Node(11), Node(12), Node(13)
five.left = three
three.left = two
six.left = eight
eight.left = eleven
twelve.left = thirteen
five.right = six
three.right = four
six.right = ten
eight.right = twelve
TreeInorder.get(five)
mirror = Solution.get_mirror_tree(five)
TreeInorder.get(mirror)
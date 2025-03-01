class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class Solution:
    @staticmethod
    def get_kth_ancestor(root: Node, node, k):
        # store the kth ancestor in a list of 1 size, assuming initially that no kth ancestor exists.
        kth = [-1]

        # recursively find the kth ancestor in O(n) time and O(h) space.
        Solution._kth_ancestor(root, node, k, kth)

        # return the kth ancestor.
        return kth[0]

    @staticmethod
    def _kth_ancestor(root: Node, node: int, k: int, kth):
        # if root is None, return None as node was not found.
        if root is None:
            return None

        # if root's data is same as node, return 1; basically we have started back tracking by 1 unit distance.
        if root.data == node:
            return 1

        # recursively check for node in left and right subtrees.
        left = Solution._kth_ancestor(root.left, node, k, kth)
        right = Solution._kth_ancestor(root.right, node, k, kth)

        # if left distance or right distance becomes equivalent to `k`, then root is the kth ancestor, update the
        # ancestor list passed by reference.
        if left == k or right == k:
            kth[0] = root.data

        # if node was not found in left and right subtrees, return None.
        if left is None and right is None:
            return None

        # if node was not found in left but in right subtree, return right + 1 to back track.
        if left is None:
            return right + 1

        # else return left + 1 for back tracking.
        return left + 1


# Example 1
eight, two, six, seven, zero, five, nine = Node(8), Node(2), Node(6), Node(7), Node(0), Node(5), Node(9)
two.left = eight
six.left = seven
eight.right = five
two.right = six
six.right = zero
zero.right = nine
print(Solution.get_kth_ancestor(two, 9, 3))

# Example 2
one, two, three, four, five = Node(1), Node(2), Node(3), Node(4), Node(5)
one.left = two
two.left = four
one.right = three
two.right = five
print(Solution.get_kth_ancestor(one, 5, 2))

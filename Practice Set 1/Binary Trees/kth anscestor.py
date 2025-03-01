class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class Solution:
    @staticmethod
    def get_kth_ancestor(root: Node, node, k):
        kth = [-1]
        Solution.kth_ancestor(root, node, k, kth)
        return kth[0]

    @staticmethod
    def kth_ancestor(root: Node, node: int, k: int, kth):
        if root is None:
            return None
        if root.data == node:
            return 1
        left = Solution.kth_ancestor(root.left, node, k, kth)
        right = Solution.kth_ancestor(root.right, node, k, kth)
        if left == k or right == k:
            kth[0] = root.data
        if left is None and right is None:
            return None
        if left is None:
            return right + 1
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

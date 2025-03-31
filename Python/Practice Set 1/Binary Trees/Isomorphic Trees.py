# Problem link - https://www.geeksforgeeks.org/problems/check-if-tree-is-isomorphic/1
# Solution - https://www.youtube.com/watch?v=9Eo42meRcrY


class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class Solution:
    @staticmethod
    def is_isomorphic(root1: Node, root2: Node):
        """
            Time complexity is O(n) and space complexity is O(h).
        """

        # if both the trees are empty, then they are isomorphic
        if root1 is None and root2 is None:
            return True

        # if one of the trees are empty, but the other is not, then they are not isomorphic
        if root1 is None or root2 is None:
            return False

        # if both the trees are not empty, then check if the data on the current node matches or not.
        # if the data does not match, return False as they are not isomorphic.
        if root1.data != root2.data:
            return False

        # finally, if the data on both the root nodes are same, use recursion on subtrees.
        # if the left subtree of 1st tree is same as left subtree of 2nd tree and right subtree of 1st tree is
        # same as right subtree of 2nd tree, then the subtrees are same-isomorphic.
        # or, if the left subtree of 1st tree is same as right subtree of 2nd tree and vice versa, then they are
        # cross-isomorphic.
        # return true if the trees are either same-isomorphic or cross-isomorphic.
        return (
            (Solution.is_isomorphic(root1.left, root2.left) and Solution.is_isomorphic(root1.right, root2.right))
            or
            (Solution.is_isomorphic(root1.left, root2.right) and Solution.is_isomorphic(root1.right, root2.left))
        )


# Example 1
one, two, three, four = Node(1), Node(2), Node(3), Node(4)
one1, two1, three1, four1 = Node(1), Node(2), Node(3), Node(4)
one.left = two
two.left = four
one.right = three
one1.left = three1
three1.left = four1
one1.right = two1
print(Solution.is_isomorphic(one, one1))

# Example 2
one, two, three, four = Node(1), Node(2), Node(3), Node(4)
one1, two1, three1, four1 = Node(1), Node(2), Node(3), Node(4)
one.left = two
two.left = four
one.right = three
one1.left = three1
one1.right = two1
two1.right = four1
print(Solution.is_isomorphic(one, one1))

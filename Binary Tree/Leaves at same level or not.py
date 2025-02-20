# Problem link - https://www.geeksforgeeks.org/check-leaves-level/


class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class Solution:
    @staticmethod
    def _perform_check(root: Node, level: int, flag: list):
        # if root is null, the method should always return True, as we don't want a single child node to return False.
        if root is None:
            return True

        # if root is leaf node
        if root.left is None and root.right is None:
            # and it is the first leaf node, denoted by flag having None, then we can return True for now.
            if flag[0] is None:
                # but update the flag
                flag[0] = level
                return True
            # if however, it is some other leaf node, return True if it is on same level, otherwise return False.
            return flag[0] == level

        # recursively check for left and right subtrees now.
        left_check = Solution._perform_check(root.left, level + 1, flag)
        right_check = Solution._perform_check(root.right, level + 1, flag)

        # return true only if both trees return True, else return False.
        return left_check and right_check

    @staticmethod
    def at_same_level(root: Node):
        """
            Time complexity is O(n) and space complexity is O(h).
        """

        # keep a reference to the level at which a leaf node is found.
        flag = [None, ]
        # perform this method call starting at level 0.
        return Solution._perform_check(root, 0, flag)


# Example 1
n1, n2, n3 = Node(1), Node(2), Node(3)
n1.left = n2
n1.right = n3
print(Solution.at_same_level(n1))

# Example 2
n10, n20, n30, n10_1, n15 = Node(10), Node(20), Node(30), Node(10), Node(15)
n10.left = n20
n10.right = n30
n20.left = n10_1
n20.right = n15
print(Solution.at_same_level(n10))

# Example 3
n1, n2, n3 = Node(1), Node(2), Node(3)
n3.left = n2
n3.right = n1
print(Solution.at_same_level(n3))

# Example 4
n12, n5, n7, n3, n1 = Node(12), Node(5), Node(7), Node(3), Node(1)
n12.left = n5
n12.right = n7
n5.left = n3
n7.right = n1
print(Solution.at_same_level(n12))

# Example 5
n12, n5, n3, n9, n1, n2 = Node(12), Node(5), Node(3), Node(9), Node(1), Node(2)
n12.left = n5
n5.left = n3
n5.right = n9
n3.left = n1
n9.left = n2
print(Solution.at_same_level(n12))

# Example 6
n12, n5, n7, n3 = Node(12), Node(5), Node(7), Node(3)
n12.left = n5
n12.right = n7
n5.left = n3
print(Solution.at_same_level(n12))

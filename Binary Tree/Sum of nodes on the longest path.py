# Problem link - https://www.geeksforgeeks.org/problems/sum-of-the-longest-bloodline-of-a-tree/1


class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class Result:
    def __init__(self, max_level, max_sum):
        self.max_level = max_level
        self.max_sum = max_sum


class Solution:
    @staticmethod
    def _solve(root, level, cumulative_sum, result):
        # if the root node is None, return from the recursion stack.
        if root is None:
            return

        # add the current node into the cumulative sum.
        cumulative_sum += root.data

        # if the max level found till now is same as this level, then take the max cumulative sum for this level.
        if level == result.max_level:
            result.max_sum = max(result.max_sum, cumulative_sum)

        # if the current level is greater than max level, reset the result.
        elif level > result.max_level:
            result.max_sum = cumulative_sum
            result.max_level = level

        # if current level < max level, nothing needs to be done.
        # now recursively solve for left and right subtrees.
        Solution._solve(root.left, level + 1, cumulative_sum, result)
        Solution._solve(root.right, level + 1, cumulative_sum, result)

    @staticmethod
    def get_sum(root: Node):
        """
            Overall time complexity is O(n) and space complexity is O(n).
        """

        # define a result object storing the max level and the max sum from the entire tree at that level.
        result = Result(-1, 0)

        # recursively find the max sum and return it.
        Solution._solve(root, 0, 0, result)
        return result.max_sum


# Example 1
n1, n2, n3, n4, n5, n6, n7 = Node(1), Node(2), Node(3), Node(4), Node(5), Node(6), Node(7)
n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n3.left = n6
n3.right = n7
print(Solution.get_sum(n1))


# Example 2
n1, n2, n3, n4, n5, n6, n7, n21 = Node(1), Node(2), Node(3), Node(4), Node(5), Node(6), Node(7), Node(2)
n4.left = n2
n4.right = n5
n2.left = n7
n2.right = n1
n1.left = n6
n5.left = n21
n5.right = n3
print(Solution.get_sum(n4))


# Example 3
n10, n5, n15, n3, n7, n20, n1 = Node(10), Node(5), Node(15), Node(3), Node(7), Node(20), Node(1)
n10.left = n5
n10.right = n15
n5.left = n3
n5.right = n7
n3.left = n1
n15.right = n20
print(Solution.get_sum(n10))

# Example 4
print(Solution.get_sum(None))

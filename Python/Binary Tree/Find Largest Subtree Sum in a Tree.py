# Problem link - https://www.geeksforgeeks.org/find-largest-subtree-sum-tree/#expected-approach-2-using-bfs-on-time-and-on-space
# Solution - https://www.youtube.com/watch?v=zm5CykXlxaA


class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class Solution:
    @staticmethod
    def _get_largest_sum(root: Node, max_tracker):
        # for null node, return 0 sum
        if root is None:
            return 0
        left_sum = Solution._get_largest_sum(root.left, max_tracker)
        right_sum = Solution._get_largest_sum(root.right, max_tracker)

        # get the subtree sum at this subtree.
        _sum = left_sum + right_sum + root.data

        # update max tracker
        max_tracker[0] = max(max_tracker[0], _sum)

        # return sum to be consistent in the return type of the recursion.
        return _sum

    @staticmethod
    def get_largest_sum(root: Node):
        """
            Time complexity is O(n) and space complexity is O(n).
        """

        max_tracker = [-1e6]
        Solution._get_largest_sum(root, max_tracker)
        return max_tracker[0]


# Example 1
n10, n8, n2, n3, n5 = Node(10), Node(8), Node(2), Node(3), Node(5)
n10.left = n8
n10.right = n2
n8.left = n3
n8.right = n5
print(Solution.get_largest_sum(n10))

# Example 2
n1, nm2, n3, n4, n5, nm6, n2 = Node(1), Node(-2), Node(3), Node(4), Node(5), Node(-6), Node(2)
n1.left = nm2
n1.right = n3
nm2.left = n4
nm2.right = n5
n3.left = nm6
n3.right = n2
print(Solution.get_largest_sum(n1))

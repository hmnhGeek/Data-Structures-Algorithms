# Problem link - https://www.geeksforgeeks.org/find-largest-subtree-sum-tree/#expected-approach-2-using-bfs-on-time-and-on-space
# Solution - https://www.youtube.com/watch?v=zm5CykXlxaA


class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class Solution:
    @staticmethod
    def get_largest_sum(root: Node):
        _sum = [-1e6]
        Solution._solve(root, _sum)
        return _sum[0]

    @staticmethod
    def _solve(root, _sum):
        """
            Time complexity is O(n) and space complexity is O(h).
        """
        if root is None:
            return 0
        left_sum = Solution._solve(root.left, _sum)
        right_sum = Solution._solve(root.right, _sum)
        curr_sum = root.data + left_sum + right_sum
        _sum[0] = max(_sum[0], curr_sum)
        return curr_sum


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

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class Solution:
    @staticmethod
    def _update_top_view(root: TreeNode, line: int, view: dict, leftmost_line: list):
        if root is None:
            return
        if line not in view:
            view[line] = root.data
            leftmost_line[0] = min(leftmost_line[0], line)

        Solution._update_top_view(root.left, line - 1, view, leftmost_line)
        Solution._update_top_view(root.right, line + 1, view, leftmost_line)

    @staticmethod
    def get_top_view(root: TreeNode):
        view = {}
        left_most_line = [0]
        Solution._update_top_view(root, 0, view, left_most_line)
        for i in range(left_most_line[0], left_most_line[0] + len(view)):
            print(view[i], end=" ")
        print()


# Example 1
n1, n2, n3, n4, n5, n6, n7 = TreeNode(1), TreeNode(2), TreeNode(3), TreeNode(4), TreeNode(5), TreeNode(6), TreeNode(7)
n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n5.left = n6
n3.right = n7
Solution.get_top_view(n1)


# Example 2
n10, n20, n30, n40, n60, n90, n100 = TreeNode(10), TreeNode(20), TreeNode(30), TreeNode(40), TreeNode(60), TreeNode(90), TreeNode(100)
n10.left = n20
n10.right = n30
n20.left = n40
n20.right = n60
n30.left = n90
n30.right = n100
Solution.get_top_view(n10)
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class Solution:
    @staticmethod
    def _update_bottom_view(root: TreeNode, level, bottom_view):
        if root is None:
            return
        bottom_view[level] = root.data
        Solution._update_bottom_view(root.left, level - 1, bottom_view)
        Solution._update_bottom_view(root.right, level + 1, bottom_view)

    @staticmethod
    def get_bottom_view(root: TreeNode):
        bottom_view = {}
        Solution._update_bottom_view(root, 0, bottom_view)
        for i in range(min(bottom_view), max(bottom_view) + 1):
            print(bottom_view[i], end=" ")
        print()


# Example 1
n20, n8, n22, n5, n3, n4, n25, n10, n14 = TreeNode(20), TreeNode(8), TreeNode(22), TreeNode(5), TreeNode(3), TreeNode(4), TreeNode(25), TreeNode(10), TreeNode(14)
n20.left = n8
n20.right = n22
n8.left = n5
n8.right = n3
n3.left = n10
n22.left = n4
n22.right = n25
n4.right = n14
Solution.get_bottom_view(n20)

# Example 2
n1, n2, n3 = TreeNode(1), TreeNode(2), TreeNode(3)
n1.left = n2
n1.right = n3
Solution.get_bottom_view(n1)

# Example 3
n10, n20, n30, n40, n60 = TreeNode(10), TreeNode(20), TreeNode(30), TreeNode(40), TreeNode(60)
n10.left = n20
n10.right = n30
n20.left = n40
n20.right = n60
Solution.get_bottom_view(n10)

# Example 4
n1, n2 = TreeNode(1), TreeNode(2)
n1.left = n2
Solution.get_bottom_view(n1)

# Example 5
n1, n2, n3, n4, n5, n6 = TreeNode(1), TreeNode(2), TreeNode(3), TreeNode(4), TreeNode(5), TreeNode(6)
n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n3.right = n6
Solution.get_bottom_view(n1)

# Example 6
n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)
n6 = TreeNode(6)
n9 = TreeNode(9)
n10 = TreeNode(10)
n11 = TreeNode(11)
n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n10
n4.right = n5
n5.right = n6
n3.left = n9
n3.right = n11
Solution.get_bottom_view(n1)

# Example 7
n2, n7, n5, n21, n6, n9, n11, n4, n51 = TreeNode(2), TreeNode(7), TreeNode(5), TreeNode(2), TreeNode(6), TreeNode(9), TreeNode(11), TreeNode(4), TreeNode(5)
n2.left = n7
n2.right = n5
n7.left = n21
n7.right = n6
n6.left = n51
n6.right = n11
n5.right = n9
n9.left = n4
Solution.get_bottom_view(n2)
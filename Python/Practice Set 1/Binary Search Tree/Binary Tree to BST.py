class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class Solution:
    @staticmethod
    def show_tree(root: Node):
        Solution._show(root)
        print()

    @staticmethod
    def _show(root: Node):
        if root:
            Solution._show(root.left)
            print(root.data, end=" ")
            Solution._show(root.right)

    @staticmethod
    def convert_to_bst(root: Node):
        """
            Time complexity is O(n * log(n)) and space complexity is O(n).
        """

        # get the nodes of the tree in inorder fashion in O(n) time and O(n) space.
        inorder = []
        Solution._get_inorder(root, inorder)

        # sort the inorder nodes data in O(n * log(n)) time.
        sorted_inorder = [i.data for i in inorder]
        sorted_inorder.sort()

        # now assign the inorder nodes with data from sorted inorder list in O(n) time.
        for i in range(len(inorder)):
            inorder[i].data = sorted_inorder[i]

    @staticmethod
    def _get_inorder(root: Node, inorder):
        if root:
            Solution._get_inorder(root.left, inorder)
            inorder.append(root)
            Solution._get_inorder(root.right, inorder)


# Example 1
n1, n2, n3 = Node(1), Node(2), Node(3)
n1.left = n2
n1.right = n3
Solution.convert_to_bst(n1)
Solution.show_tree(n1)

# Example 2
n1, n2, n3, n4 = Node(1), Node(2), Node(3), Node(4)
n1.left = n2
n2.left = n4
n1.right = n3
Solution.convert_to_bst(n1)
Solution.show_tree(n1)

# Example 3
n10, n2, n7, n8, n4 = Node(10), Node(2), Node(7), Node(8), Node(4)
n10.left = n2
n10.right = n7
n2.left = n8
n2.right = n4
Solution.convert_to_bst(n10)
Solution.show_tree(n10)

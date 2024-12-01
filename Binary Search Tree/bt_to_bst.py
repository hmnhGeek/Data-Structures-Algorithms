# Problem link - https://www.geeksforgeeks.org/problems/binary-tree-to-bst/1


class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class Solution:
    @staticmethod
    def _get_inorder(root, inorder):
        if root:
            Solution._get_inorder(root.left, inorder)
            inorder.append(root)
            Solution._get_inorder(root.right, inorder)

    @staticmethod
    def _show(root):
        if root:
            Solution._show(root.left)
            print(root.data, end=" ")
            Solution._show(root.right)

    @staticmethod
    def convert_to_bst(root: Node):
        """
            Time complexity is O(nlog(n)) and space complexity is O(n).
        """

        # get the inorder nodes of the tree in O(n) time and O(h + n) space.
        inorder_nodes = []
        Solution._get_inorder(root, inorder_nodes)

        # get data points in O(n) time and O(n) space.
        inorder_data = [i.data for i in inorder_nodes]

        # sort the data points in O(nlog(n)) time.
        inorder_data.sort()

        # loop in the inorder traversal and assign the sorted data points in O(n) time.
        for i in range(len(inorder_data)):
            inorder_nodes[i].data = inorder_data[i]

        # print the BST.
        Solution._show(root)
        print()


# Example 1
n1, n2, n3 = Node(1), Node(2), Node(3)
n1.left = n2
n1.right = n3
Solution.convert_to_bst(n1)

# Example 2
n1, n2, n3, n4 = Node(1), Node(2), Node(3), Node(4)
n1.left = n2
n2.left = n4
n1.right = n3
Solution.convert_to_bst(n1)

# Example 3
n10, n2, n7, n8, n4 = Node(10), Node(2), Node(7), Node(8), Node(4)
n10.left = n2
n10.right = n7
n2.left = n8
n2.right = n4
Solution.convert_to_bst(n10)

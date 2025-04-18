# Problem link - https://www.geeksforgeeks.org/problems/binary-tree-to-bst/1


class QuickSort:
    @staticmethod
    def sort(arr):
        QuickSort._sort(arr, 0, len(arr) - 1)

    @staticmethod
    def _sort(arr, low, high):
        if low >= high:
            return
        partition_index = QuickSort._get_partition_index(arr, low, high)
        QuickSort._sort(arr, low, partition_index - 1)
        QuickSort._sort(arr, partition_index + 1, high)

    @staticmethod
    def _get_partition_index(arr, low, high):
        pivot = arr[low]
        i, j = low, high
        while i < j:
            while arr[i] <= pivot and i <= high - 1:
                i += 1
            while arr[j] > pivot and j >= low + 1:
                j -= 1
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]
        arr[low], arr[j] = arr[j], arr[low]
        return j


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
        QuickSort.sort(sorted_inorder)

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

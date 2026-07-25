class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class QuickSort:
    @staticmethod
    def sort(arr):
        n = len(arr)
        QuickSort._sort(arr, 0, n - 1)

    @staticmethod
    def _sort(arr, low, high):
        if low >= high:
            return
        partition_index = QuickSort._get_partition_index(arr, low, high)
        QuickSort._sort(arr, low, partition_index - 1)
        QuickSort._sort(arr, partition_index + 1, high)

    @staticmethod
    def _get_partition_index(arr, low, high):
        i, j = low, high
        pivot = arr[low]
        while i < j:
            while arr[i] <= pivot and i <= high - 1:
                i += 1
            while arr[j] > pivot and j >= low + 1:
                j -= 1
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]
        arr[j], arr[low] = arr[low], arr[j]
        return j


class Solution:
    @staticmethod
    def convert_to_bst(root: Node):
        inorder = []
        Solution._get_inorder_data(root, inorder)
        QuickSort.sort(inorder)
        nodes = []
        Solution._get_nodes(root, nodes)
        i = 0
        for node in nodes:
            node.data = inorder[i]
            i += 1
    
    @staticmethod
    def show(root: Node):
        if root is not None:
            Solution.show(root.left)
            print(root.data)
            Solution.show(root.right)

    @staticmethod
    def _get_inorder_data(root, inorder):
        if root:
            Solution._get_inorder_data(root.left, inorder)
            inorder.append(root.data)
            Solution._get_inorder_data(root.right, inorder)

    @staticmethod
    def _get_nodes(root, nodes):
        if root:
            Solution._get_nodes(root.left, nodes)
            nodes.append(root)
            Solution._get_nodes(root.right, nodes)
            

# Example 1
n1, n2, n3 = Node(1), Node(2), Node(3)
n1.left = n2
n1.right = n3
Solution.convert_to_bst(n1)
Solution.show(n1)
print()

# Example 2
n1, n2, n3, n4 = Node(1), Node(2), Node(3), Node(4)
n1.left = n2
n2.left = n4
n1.right = n3
Solution.convert_to_bst(n1)
Solution.show(n1)
print()

# Example 3
n10, n2, n7, n8, n4 = Node(10), Node(2), Node(7), Node(8), Node(4)
n10.left = n2
n10.right = n7
n2.left = n8
n2.right = n4
Solution.convert_to_bst(n10)
Solution.show(n10)
print()

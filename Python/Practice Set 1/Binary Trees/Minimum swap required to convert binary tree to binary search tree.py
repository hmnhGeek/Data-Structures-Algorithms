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
        pivot = arr[low]
        i, j = low, high
        while i < j:
            while arr[i] <= pivot and i <= high - 1:
                i += 1
            while arr[j] > pivot and j >= low + 1:
                j -= 1
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]
        arr[j], arr[low] = arr[low], arr[j]
        return j


class Util:
    @staticmethod
    def _swap(arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]

    @staticmethod
    def min_swaps_to_sort(arr):
        n = len(arr)
        helper_arr = [(arr[i], i) for i in range(n)]
        QuickSort.sort(helper_arr)
        count_swaps = 0
        for i in range(n):
            if helper_arr[i][1] != i:
                Util._swap(helper_arr, i, helper_arr[i][1])
                count_swaps += 1
                i -= 1
        return count_swaps


class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class Solution:
    @staticmethod
    def min_swaps_to_bst(root: Node) -> int:
        inorder = []
        Solution._get_inorder(root, inorder)
        return Util.min_swaps_to_sort(inorder)

    @staticmethod
    def _get_inorder(root, inorder):
        if root:
            Solution._get_inorder(root.left, inorder)
            inorder.append(root.data)
            Solution._get_inorder(root.right, inorder)


# Example 1
n5, n6, n7, n8, n9, n10, n11 = Node(5), Node(6), Node(7), Node(8), Node(9), Node(10), Node(11)
n5.left = n6
n5.right = n7
n6.left = n8
n6.right = n9
n7.left = n10
n7.right = n11
print(Solution.min_swaps_to_bst(n5))


# Example 2
n1, n2, n3 = Node(1), Node(2), Node(3)
n1.left = n2
n1.right = n3
print(Solution.min_swaps_to_bst(n1))

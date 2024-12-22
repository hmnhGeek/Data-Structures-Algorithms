class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class Solution:
    @staticmethod
    def _get_inorder(root: Node, inorder):
        if root:
            Solution._get_inorder(root.left, inorder)
            inorder.append(root.data)
            Solution._get_inorder(root.right, inorder)

    @staticmethod
    def _get_min_swaps(inorder: list):
        temp = [(inorder[i], i) for i in range(len(inorder))]
        temp.sort(key=lambda x: x[0])
        i = 0
        swaps = 0
        while i < len(temp):
            elem, index = temp[i]
            if index != i:
                temp[index], temp[i] = temp[i], temp[index]
                swaps += 1
            else:
                i += 1
        return swaps

    @staticmethod
    def get_min_swaps(root: Node):
        inorder = []
        Solution._get_inorder(root, inorder)
        return Solution._get_min_swaps(inorder)


# Example 1
n5, n6, n7, n8, n9, n10, n11 = Node(5), Node(6), Node(7), Node(8), Node(9), Node(10), Node(11)
n5.left = n6
n5.right = n7
n6.left = n8
n6.right = n9
n7.left = n10
n7.right = n11
print(Solution.get_min_swaps(n5))


# Example 2
n1, n2, n3 = Node(1), Node(2), Node(3)
n1.left = n2
n1.right = n3
print(Solution.get_min_swaps(n1))

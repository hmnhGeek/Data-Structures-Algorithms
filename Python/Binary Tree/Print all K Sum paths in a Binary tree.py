# Problem link - https://www.geeksforgeeks.org/print-k-sum-paths-binary-tree/
# Solution - https://www.youtube.com/watch?v=_Ng486jJu80


class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class Solution:
    @staticmethod
    def _find(root, k, paths):
        if root is None:
            return
        paths.append(root.data)
        Solution._find(root.left, k, paths)
        Solution._find(root.right, k, paths)
        _sum = 0
        for i in range(-1, -len(paths) - 1, -1):
            _sum += paths[i]
            if _sum == k:
                print(paths[i:])
        paths.pop(-1)

    @staticmethod
    def find_sum(root, k):
        paths = []
        Solution._find(root, k, paths)


# Example
n10, n3, nm1, n20, n11, n4, n5, n12, n13, n21, n6 = Node(1), Node(3), Node(-1), Node(2), Node(1), Node(4), Node(5), Node(1), Node(1), Node(2), Node(6)
n14 = Node(1)
n10.left = n3
n10.right = nm1
n3.left = n20
n3.right = n12
nm1.left = n4
nm1.right = n5
n12.left = n13
n4.left = n14
n4.right = n21
n5.right = n6
Solution.find_sum(n10, 5)

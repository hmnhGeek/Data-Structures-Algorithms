# Problem link - https://www.geeksforgeeks.org/problems/is-binary-tree-heap/1
# Solution - https://www.youtube.com/watch?v=jX-UP7b2bkk


class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None
        

class Solution:
    @staticmethod
    def _get_size(root: Node):
        if root is None:
            return 0
        return 1 + Solution._get_size(root.left) + Solution._get_size(root.right)
    
    @staticmethod
    def is_max_heap(root: Node):
        """
            Time complexity is O(n) and space complexity is O(n)
        """
        if root is None:
            return True
        n = Solution._get_size(root)
        return Solution._is_max_heap(root) and Solution._is_complete(root, 0, n)
    
    @staticmethod
    def _is_max_heap(root):
        if root is None:
            return True
        if root.left is not None and root.left.data > root.data:
            return False
        if root.right is not None and root.right.data > root.data:
            return False
        return Solution._is_max_heap(root.left) and Solution._is_max_heap(root.right)
    
    @staticmethod
    def _is_complete(root: Node, i: int, n: int):
        if root is None:
            return True
        if i + 1 > n:
            return False
        return Solution._is_complete(root.left, 2*i + 1, n) and Solution._is_complete(root.right, 2*i + 2, n)


# Example 1
n10, n20, n30, n40, n60 = Node(10), Node(20), Node(30), Node(40), Node(60)
n10.left = n20
n10.right = n30
n20.left = n40
n20.right = n60
print(Solution.is_max_heap(n10))


# Example 2
n5, n2, n3 = Node(5), Node(2), Node(3)
n5.left = n2
n5.right = n3
print(Solution.is_max_heap(n5))


# Example 3
n40 = Node(40)
n36 = Node(36)
n23 = Node(23)
n10 = Node(10)
n23_1 = Node(23)
n5 = Node(5)
n6 = Node(6)
n1 = Node(1)
n14 = Node(14)
n40.left = n36
n40.right = n23
n36.left = n10
n36.right = n23_1
n23.left = n5
n23.right = n6
n10.left = n1
n10.right = n14
print(Solution.is_max_heap(n40))


# Example 4
n40 = Node(40)
n36 = Node(36)
n23 = Node(23)
n10 = Node(10)
n5 = Node(5)
n6 = Node(6)
n1 = Node(1)
n14 = Node(14)
n40.left = n36
n40.right = n23
n36.left = n10
n23.left = n5
n23.right = n6
n10.left = n1
n5.left = n14
print(Solution.is_max_heap(n40))


# Example 5
n15 = Node(15)
n14 = Node(14)
n10 = Node(10)
n4 = Node(4)
n5 = Node(5)
n11 = Node(11)
n5_1 = Node(5)
n1 = Node(1)
n2 = Node(2)
n15.left = n14
n15.right = n10
n14.left = n4
n14.right = n5
n10.left = n11
n10.right = n5
n4.left = n1
n4.right = n2
print(Solution.is_max_heap(n15))

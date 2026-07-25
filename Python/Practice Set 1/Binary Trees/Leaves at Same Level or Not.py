class LevelTracker:
    def __init__(self):
        self.level = None
        self.same_level = True


class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class Solution:
    @staticmethod
    def at_same_level(root: Node):
        obj = LevelTracker()
        Solution._solve(root, 0, obj)
        return obj.same_level

    @staticmethod
    def _solve(root: Node, level: int, obj: LevelTracker):
        if root is None:
            return
        if root.left is None and root.right is None:
            if obj.level is None:
                obj.level = level
                return
            elif obj.level != level:
                obj.same_level = False
                return
        Solution._solve(root.left, level + 1, obj)
        Solution._solve(root.right, level + 1, obj)


# Example 1
n1, n2, n3 = Node(1), Node(2), Node(3)
n1.left = n2
n1.right = n3
print(Solution.at_same_level(n1))

# Example 2
n10, n20, n30, n10_1, n15 = Node(10), Node(20), Node(30), Node(10), Node(15)
n10.left = n20
n10.right = n30
n20.left = n10_1
n20.right = n15
print(Solution.at_same_level(n10))

# Example 3
n1, n2, n3 = Node(1), Node(2), Node(3)
n3.left = n2
n3.right = n1
print(Solution.at_same_level(n3))

# Example 4
n12, n5, n7, n3, n1 = Node(12), Node(5), Node(7), Node(3), Node(1)
n12.left = n5
n12.right = n7
n5.left = n3
n7.right = n1
print(Solution.at_same_level(n12))

# Example 5
n12, n5, n3, n9, n1, n2 = Node(12), Node(5), Node(3), Node(9), Node(1), Node(2)
n12.left = n5
n5.left = n3
n5.right = n9
n3.left = n1
n9.left = n2
print(Solution.at_same_level(n12))

# Example 6
n12, n5, n7, n3 = Node(12), Node(5), Node(7), Node(3)
n12.left = n5
n12.right = n7
n5.left = n3
print(Solution.at_same_level(n12))

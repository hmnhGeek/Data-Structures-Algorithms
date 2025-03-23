class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class Solution:
    @staticmethod
    def is_isomorphic(root1: Node, root2: Node):
        if root1 is None and root2 is None:
            return True
        if root1 is None or root2 is None:
            return False
        if root1.data != root2.data:
            return False
        return (
            (Solution.is_isomorphic(root1.left, root2.left) and Solution.is_isomorphic(root1.right, root2.right))
            or
            (Solution.is_isomorphic(root1.left, root2.right) and Solution.is_isomorphic(root1.right, root2.left))
        )


# Example 1
one, two, three, four = Node(1), Node(2), Node(3), Node(4)
one1, two1, three1, four1 = Node(1), Node(2), Node(3), Node(4)
one.left = two
two.left = four
one.right = three
one1.left = three1
three1.left = four1
one1.right = two1
print(Solution.is_isomorphic(one, one1))

# Example 2
one, two, three, four = Node(1), Node(2), Node(3), Node(4)
one1, two1, three1, four1 = Node(1), Node(2), Node(3), Node(4)
one.left = two
two.left = four
one.right = three
one1.left = three1
one1.right = two1
two1.right = four1
print(Solution.is_isomorphic(one, one1))

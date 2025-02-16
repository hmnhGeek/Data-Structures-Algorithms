class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class Solution:
    @staticmethod
    def get_lca(root: Node, x, y):
        # if a null node is reached, return null.
        if root is None:
            return

        # if root's data is either x or y, check no further, just return x or y.
        if root.data == x:
            return x
        if root.data == y:
            return y

        # recursively call this method for left and right subtrees.
        left = Solution.get_lca(root.left, x, y)
        right = Solution.get_lca(root.right, x, y)

        # if both subtrees return None, the two nodes were not found in the subtrees, thus return None.
        if left is None and right is None:
            return

        # if left subtree did not have the nodes, return None.
        if left is None:
            return right

        # if right subtree did not have the nodes, return None.
        if right is None:
            return left

        # since both of them returned non-None, both the nodes have been found and therefore, this root node is their
        # LCA; return it.
        return root.data


one, two, three, four, five, six, svn, eight = Node(1), Node(2), Node(3), Node(4), Node(5), Node(6), Node(7), Node(8)

one.left = two
three.left = four
four.left = eight
five.left = six

one.right = three
three.right = five
five.right = svn

print(Solution.get_lca(one, 7, 8))
print(Solution.get_lca(one, 4, 8))
print(Solution.get_lca(one, None, 2))
print(Solution.get_lca(one, 6, 3))

# Example 2
z, o, t, th, f, fi, s, sv, e = [Node(i) for i in range(9)]
th.left = fi
th.right = o
fi.left = s
fi.right = t
o.left = z
o.right = e
t.left = sv
t.right = f
print(Solution.get_lca(th, 5, 1))
print(Solution.get_lca(th, 5, 4))

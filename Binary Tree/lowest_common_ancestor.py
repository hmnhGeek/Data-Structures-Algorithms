# Problem link - https://www.geeksforgeeks.org/problems/lowest-common-ancestor-in-a-binary-tree/1
# Solution - https://www.youtube.com/watch?v=_-QHfMDde90


class Node:
    def __init__(self, data: int):
        self.data = data
        self.left = None
        self.right = None


class LowestCommonAncestorFinder:
    # The time complexity is O(N) as we will be traversing the whole tree with a space complexity of O(H), as at any
    # given point, the deepest recursion stack is `H` length deep.

    def __init__(self, root: Node | None):
        self.root = root

    def _recursive_find_lcs(self, root: Node | None, node1: Node | None, node2: Node | None) -> Node | None:
        # The algorithm is this:
        # 1. If both left and right subtrees return None, then return None at root.
        # 2. If either one of the subtrees return a non-None node, return that node from root.
        # 3. If both the nodes return some non-None nodes, return the root node from root.
        # At the end, whatever the root of the tree returns is the LCS.
        # Also note that a non-None node will be returned only if node1 or node2 are found.

        # if at any point you're on a None node, return None
        if root is None:
            return None

        # if either node1 or node2 is found, look no deeper, return this node.
        if root == node1:
            return node1

        if root == node2:
            return node2

        # look for node1 and node2 in left and right subtrees
        left_recursion = self._recursive_find_lcs(root.left, node1, node2)
        right_recursion = self._recursive_find_lcs(root.right, node1, node2)

        # follow the algorithm written above.
        if left_recursion is None and right_recursion is None:
            return None
        if left_recursion is None:
            return right_recursion
        if right_recursion is None:
            return left_recursion
        return root

    def find_lcs(self, node1: Node | None, node2: Node | None) -> Node | None:
        # stand at root node and start recursing on the tree to find LCS
        curr = self.root
        return self._recursive_find_lcs(curr, node1, node2)


one, two, three, four, five, six, svn, eight = Node(1), Node(2), Node(3), Node(4), Node(5), Node(6), Node(7), Node(8)

one.left = two
three.left = four
four.left = eight
five.left = six

one.right = three
three.right = five
five.right = svn

lcs_finder = LowestCommonAncestorFinder(one)
lcs = lcs_finder.find_lcs(svn, eight)
print(lcs.data if lcs else None)
lcs2 = lcs_finder.find_lcs(eight, four)
print(lcs2.data if lcs2 else None)
lcs3 = lcs_finder.find_lcs(None, two)
print(lcs3.data if lcs3 else None)
lcs4 = lcs_finder.find_lcs(six, three)
print(lcs4.data if lcs4 else None)

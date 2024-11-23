# Problem link - https://www.geeksforgeeks.org/problems/is-binary-tree-heap/1
# Solution - https://www.youtube.com/watch?v=5zyG8Nw9V78 (Complete binary tree check using DFS)
# Solution - https://www.youtube.com/watch?v=08e5EBHoXxE (Complete binary tree check using BFS)


class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class Solution:
    @staticmethod
    def _count_nodes_in_tree(root: Node) -> int:
        if root is None:
            return 0
        return 1 + Solution._count_nodes_in_tree(root.left) + Solution._count_nodes_in_tree(root.right)

    @staticmethod
    def _is_max_heap(root: Node, index: int, num_nodes: int) -> bool:
        # if the root node is None, return True as a null node is a max heap only.
        if root is None:
            return True
        # if at any point, the index is more than equal to the number of nodes, then it would mean that at the current
        # level, there are NULL nodes in between two or more non-NULL nodes. This means the tree is not a complete
        # binary tree. Therefore, return False.
        if index >= num_nodes:
            return False

        # now check if the root node data is maximum or not. Here, we mark root node maximum even if the left child is
        # None but right is not, provided the right child is smaller or equal to the root node's data. We know that
        # would be an incomplete binary tree, but that check would take place in the base cases above, so no need to
        # specially handle this case here.
        root_node_is_max = (
            root.data >= root.left.data if root.left else -1e6 and
            root.data >= root.right.data if root.right else -1e6
        )

        # finally, the tree is a max heap if root node is maximum compared to its left and right children and if the
        # tree is a complete binary tree.
        return (
            root_node_is_max and
            Solution._is_max_heap(root.left, 2*index + 1, num_nodes) and
            Solution._is_max_heap(root.right, 2*index + 2, num_nodes)
        )

    @staticmethod
    def validate_if_max_heap(root: Node) -> bool:
        """
            Overall time complexity is O(n) and space complexity is O(h).
        """

        # count the number of nodes in the binary tree in O(n) time and O(h) recursion space.
        num_nodes = Solution._count_nodes_in_tree(root)
        # assign the root node with index 0.
        index = 0
        # recursively check from the root node if the tree is a max heap or not. This will also take O(n) time and O(h)
        # recursion stack space.
        return Solution._is_max_heap(root, index, num_nodes)


# Example 1
n10, n20, n30, n40, n60 = Node(10), Node(20), Node(30), Node(40), Node(60)
n10.left = n20
n10.right = n30
n20.left = n40
n20.right = n60
print(Solution.validate_if_max_heap(n10))


# Example 2
n5, n2, n3 = Node(5), Node(2), Node(3)
n5.left = n2
n5.right = n3
print(Solution.validate_if_max_heap(n5))

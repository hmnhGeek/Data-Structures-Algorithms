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
        if root is None:
            return True
        if index >= num_nodes:
            return False

        root_node_is_max = (
            root.data >= root.left.data if root.left else -1e6 and
            root.data >= root.right.data if root.right else -1e6
        )
        return (
            root_node_is_max and
            Solution._is_max_heap(root.left, 2*index + 1, num_nodes) and
            Solution._is_max_heap(root.right, 2*index + 2, num_nodes)
        )

    @staticmethod
    def validate_if_max_heap(root: Node) -> bool:
        num_nodes = Solution._count_nodes_in_tree(root)
        index = 0
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
